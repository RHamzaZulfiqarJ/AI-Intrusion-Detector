from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import torch
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)

from src.training.metrics import Metrics
from src.utils.logger import logger


class Evaluator:

    def __init__(
        self,
        model: torch.nn.Module,
        test_loader,
        checkpoint_path: str,
        output_dir: str = "artifacts/evaluation",
    ):

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = model.to(self.device)

        self.test_loader = test_loader

        self.checkpoint_path = checkpoint_path

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load_checkpoint(self):

        logger.info(
            "Loading best checkpoint..."
        )

        checkpoint = torch.load(
            self.checkpoint_path,
            map_location=self.device,
        )

        self.model.load_state_dict(
            checkpoint["model_state_dict"]
        )

    @torch.no_grad()
    def evaluate(self):

        self.load_checkpoint()

        self.model.eval()

        predictions = []

        labels = []

        for features, target in self.test_loader:

            features = features.to(self.device)

            outputs = self.model(features)

            prediction = outputs.argmax(dim=1)

            predictions.extend(
                prediction.cpu().numpy()
            )

            labels.extend(
                target.numpy()
            )

        predictions = torch.tensor(predictions)

        labels = torch.tensor(labels)

        metrics = {
            "accuracy": Metrics.accuracy(
                predictions,
                labels,
            ),
            "precision": Metrics.precision(
                predictions,
                labels,
            ),
            "recall": Metrics.recall(
                predictions,
                labels,
            ),
            "f1_score": Metrics.f1(
                predictions,
                labels,
            ),
        }

        with open(
            self.output_dir / "metrics.json",
            "w",
        ) as file:

            json.dump(
                metrics,
                file,
                indent=4,
            )

        report = classification_report(
            labels.numpy(),
            predictions.numpy(),
            output_dict=True,
            zero_division=0,
        )

        report_df = pd.DataFrame(report).transpose()

        report_df.to_csv(
            self.output_dir /
            "classification_report.csv"
        )

        cm = confusion_matrix(
            labels.numpy(),
            predictions.numpy(),
        )

        fig, ax = plt.subplots(
            figsize=(10, 10)
        )

        ConfusionMatrixDisplay(
            confusion_matrix=cm,
        ).plot(
            ax=ax,
            xticks_rotation=90,
            colorbar=False,
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "confusion_matrix.png",
            dpi=300,
        )

        plt.close()

        logger.info(
            "Evaluation completed."
        )

        return metrics