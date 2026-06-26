from __future__ import annotations

from pathlib import Path

import torch

from src.utils.logger import logger


class ModelCheckpoint:

    def __init__(
        self,
        checkpoint_dir: str = "training/checkpoints",
        monitor: str = "validation_loss",
        mode: str = "min",
    ):

        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.monitor = monitor
        self.mode = mode

        if mode == "min":
            self.best_score = float("inf")
        else:
            self.best_score = float("-inf")

    def __call__(
        self,
        epoch: int,
        score: float,
        model: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
    ):

        improved = (
            score < self.best_score
            if self.mode == "min"
            else score > self.best_score
        )

        if improved:

            self.best_score = score

            checkpoint_path = (
                self.checkpoint_dir /
                "best_model.pth"
            )

            torch.save(
                {
                    "epoch": epoch,
                    "score": score,
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": optimizer.state_dict(),
                },
                checkpoint_path,
            )

            logger.info(
                f"Checkpoint saved: {checkpoint_path}"
            )


class EarlyStopping:

    def __init__(
        self,
        patience: int = 5,
        min_delta: float = 0.0,
        mode: str = "min",
    ):

        self.patience = patience
        self.min_delta = min_delta
        self.mode = mode

        self.counter = 0

        if mode == "min":
            self.best_score = float("inf")
        else:
            self.best_score = float("-inf")

        self.should_stop = False

    def __call__(
        self,
        score: float,
    ) -> bool:

        if self.mode == "min":

            improved = (
                score <
                self.best_score - self.min_delta
            )

        else:

            improved = (
                score >
                self.best_score + self.min_delta
            )

        if improved:

            self.best_score = score
            self.counter = 0

        else:

            self.counter += 1

            if self.counter >= self.patience:

                self.should_stop = True

        return self.should_stop