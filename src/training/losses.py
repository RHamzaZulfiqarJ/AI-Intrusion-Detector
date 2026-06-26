from __future__ import annotations

import torch
import torch.nn as nn


class LossFactory:
    """
    Factory class for creating loss functions.
    """

    @staticmethod
    def cross_entropy(
        class_weights: torch.Tensor | None = None,
    ) -> nn.Module:

        if class_weights is not None:

            return nn.CrossEntropyLoss(
                weight=class_weights,
            )

        return nn.CrossEntropyLoss()

    @staticmethod
    def focal_loss(
        alpha: float = 1.0,
        gamma: float = 2.0,
    ):

        class FocalLoss(nn.Module):

            def __init__(self):

                super().__init__()

                self.alpha = alpha
                self.gamma = gamma

                self.ce = nn.CrossEntropyLoss(
                    reduction="none"
                )

            def forward(
                self,
                outputs,
                targets,
            ):

                ce_loss = self.ce(
                    outputs,
                    targets,
                )

                pt = torch.exp(-ce_loss)

                loss = (
                    self.alpha
                    * (1 - pt) ** self.gamma
                    * ce_loss
                )

                return loss.mean()

        return FocalLoss()