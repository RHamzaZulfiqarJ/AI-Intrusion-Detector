from __future__ import annotations

import mlflow

import torch
from torch.utils.data import DataLoader

from src.training.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
)
from src.training.losses import LossFactory
from src.training.metrics import Metrics
from src.training.model import IntrusionDetectionModel
from src.utils.logger import logger

from src.mlops import ModelRegistry
from src.mlops import ExperimentManager
from src.mlops import SystemLogger
from src.mlops import MLflowLogger
from src.mlops import ArtifactLogger
from src.mlops import DatasetLogger

import pandas as pd

class Trainer:

    def __init__(
        self,
        model: IntrusionDetectionModel,
        train_loader: DataLoader,
        validation_loader: DataLoader,
        learning_rate: float = 1e-3,
        epochs: int = 20,
        train_df: pd.DataFrame | None = None,
        validation_df: pd.DataFrame | None = None,
        test_df: pd.DataFrame | None = None,
    ):
        self.learning_rate = learning_rate
        self.experiment = ExperimentManager()
        self.train_df = train_df
        self.validation_df = validation_df
        self.test_df = test_df

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        logger.info(
            f"Using device: {self.device}"
        )

        self.model = model.to(self.device)

        self.train_loader = train_loader

        self.validation_loader = validation_loader

        self.epochs = epochs

        self.criterion = LossFactory.cross_entropy()

        self.optimizer = torch.optim.Adam(
            self.model.parameters(),
            lr=learning_rate,
        )

        self.checkpoint = ModelCheckpoint(
            monitor="validation_loss",
            mode="min",
        )

        self.early_stopping = EarlyStopping(
            patience=5,
            mode="min",
        )

    def train_one_epoch(self):

        self.model.train()

        running_loss = 0.0

        predictions = []

        labels_list = []

        for features, labels in self.train_loader:

            features = features.to(self.device)

            labels = labels.to(self.device)

            self.optimizer.zero_grad()

            outputs = self.model(features)

            loss = self.criterion(
                outputs,
                labels,
            )

            loss.backward()

            self.optimizer.step()

            running_loss += loss.item()

            predictions.append(
                outputs.argmax(dim=1).cpu()
            )

            labels_list.append(
                labels.cpu()
            )

        predictions = torch.cat(predictions)

        labels = torch.cat(labels_list)

        epoch_loss = (
            running_loss /
            len(self.train_loader)
        )

        epoch_accuracy = Metrics.accuracy(
            predictions,
            labels,
        )

        epoch_f1 = Metrics.f1(
            predictions,
            labels,
        )

        return (
            epoch_loss,
            epoch_accuracy,
            epoch_f1,
        )

    @torch.no_grad()
    def validate(self):

        self.model.eval()

        running_loss = 0.0

        predictions = []

        labels_list = []

        for features, labels in self.validation_loader:

            features = features.to(self.device)

            labels = labels.to(self.device)

            outputs = self.model(features)

            loss = self.criterion(
                outputs,
                labels,
            )

            running_loss += loss.item()

            predictions.append(
                outputs.argmax(dim=1).cpu()
            )

            labels_list.append(
                labels.cpu()
            )

        predictions = torch.cat(predictions)

        labels = torch.cat(labels_list)

        validation_loss = (
            running_loss /
            len(self.validation_loader)
        )

        validation_accuracy = Metrics.accuracy(
            predictions,
            labels,
        )

        validation_f1 = Metrics.f1(
            predictions,
            labels,
        )

        return (
            validation_loss,
            validation_accuracy,
            validation_f1,
        )

    def train(self):

        logger.info(
            "Starting training..."
        )

        history = {
            "train_loss": [],
            "validation_loss": [],
            "train_accuracy": [],
            "validation_accuracy": [],
            "train_f1": [],
            "validation_f1": [],
        }

        with self.experiment.start_run():

            SystemLogger.log()

            MLflowLogger.log_params({
                "learning_rate": self.learning_rate,
                "epochs": self.epochs,
                "input_dim": self.model.input_dim,
                "num_classes": self.model.num_classes,
                "batch_size": self.train_loader.batch_size,
                "optimizer": type(self.optimizer).__name__,
                "loss": type(self.criterion).__name__,
            })

            if (
                self.train_df is not None
                and self.validation_df is not None
                and self.test_df is not None
            ):
                DatasetLogger.log(
                    self.train_df,
                    self.validation_df,
                    self.test_df,
                )

            for epoch in range(
                1,
                self.epochs + 1,
            ):

                (
                    train_loss,
                    train_accuracy,
                    train_f1,
                ) = self.train_one_epoch()

                (
                    validation_loss,
                    validation_accuracy,
                    validation_f1,
                ) = self.validate()

                history["train_loss"].append(train_loss)
                history["validation_loss"].append(validation_loss)

                history["train_accuracy"].append(train_accuracy)
                history["validation_accuracy"].append(validation_accuracy)

                history["train_f1"].append(train_f1)
                history["validation_f1"].append(validation_f1)

                MLflowLogger.log_metrics(
                    {
                        "train_loss": train_loss,
                        "validation_loss": validation_loss,
                        "train_accuracy": train_accuracy,
                        "validation_accuracy": validation_accuracy,
                        "train_f1": train_f1,
                        "validation_f1": validation_f1,
                    },
                    step=epoch,
                )

                logger.info(
                    f"Epoch [{epoch}/{self.epochs}] | "
                    f"Train Loss: {train_loss:.4f} | "
                    f"Train Acc: {train_accuracy:.4f} | "
                    f"Train F1: {train_f1:.4f} | "
                    f"Val Loss: {validation_loss:.4f} | "
                    f"Val Acc: {validation_accuracy:.4f} | "
                    f"Val F1: {validation_f1:.4f}"
                )

                self.checkpoint(
                    epoch,
                    validation_loss,
                    self.model,
                    self.optimizer,
                )

                if self.early_stopping(
                    validation_loss,
                ):

                    logger.info(
                        "Early stopping triggered."
                    )

                    break

            logger.info(
                "Training completed."
            )

            ArtifactLogger.log_if_exists(
                "artifacts/evaluation",
                "artifacts/metadata",
                "artifacts/encoders",
                "artifacts/scalers",
            )

            example = torch.randn(
                1,
                self.model.input_dim,
                device=self.device,
            )

            ModelRegistry.register(
                model=self.model,
                input_example=example,
            )

        return history