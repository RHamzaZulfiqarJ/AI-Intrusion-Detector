from __future__ import annotations

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


class Metrics:

    @staticmethod
    def accuracy(
        predictions: torch.Tensor,
        labels: torch.Tensor,
    ) -> float:

        predictions = predictions.cpu().numpy()
        labels = labels.cpu().numpy()

        return accuracy_score(
            labels,
            predictions,
        )

    @staticmethod
    def precision(
        predictions: torch.Tensor,
        labels: torch.Tensor,
        average: str = "weighted",
    ) -> float:

        predictions = predictions.cpu().numpy()
        labels = labels.cpu().numpy()

        return precision_score(
            labels,
            predictions,
            average=average,
            zero_division=0,
        )

    @staticmethod
    def recall(
        predictions: torch.Tensor,
        labels: torch.Tensor,
        average: str = "weighted",
    ) -> float:

        predictions = predictions.cpu().numpy()
        labels = labels.cpu().numpy()

        return recall_score(
            labels,
            predictions,
            average=average,
            zero_division=0,
        )

    @staticmethod
    def f1(
        predictions: torch.Tensor,
        labels: torch.Tensor,
        average: str = "weighted",
    ) -> float:

        predictions = predictions.cpu().numpy()
        labels = labels.cpu().numpy()

        return f1_score(
            labels,
            predictions,
            average=average,
            zero_division=0,
        )

    @staticmethod
    def confusion(
        predictions: torch.Tensor,
        labels: torch.Tensor,
    ) -> np.ndarray:

        predictions = predictions.cpu().numpy()
        labels = labels.cpu().numpy()

        return confusion_matrix(
            labels,
            predictions,
        )