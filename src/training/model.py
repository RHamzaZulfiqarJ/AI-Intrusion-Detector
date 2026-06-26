from __future__ import annotations

from pathlib import Path

import torch
import torch.nn as nn


class IntrusionDetectionModel(nn.Module):
    """
    Baseline Feed-Forward Neural Network for CICIDS2017.
    """

    def __init__(
        self,
        input_dim: int = 70,
        num_classes: int = 15,
        dropout: float = 0.3,
    ):
        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.BatchNorm1d(256),
            nn.Dropout(dropout),

            nn.Linear(256, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(dropout),

            nn.Linear(128, 64),
            nn.ReLU(),
            nn.BatchNorm1d(64),
            nn.Dropout(dropout),

            nn.Linear(64, num_classes),
        )

    def forward(self, x):

        return self.network(x)
    
    def load_weights(
        self,
        checkpoint_path: str | Path,
        device: str = "cpu",
    ):

        checkpoint = torch.load(
            checkpoint_path,
            map_location=device,
        )

        # Handle both plain state_dict and checkpoint dictionaries
        if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:

            self.load_state_dict(
                checkpoint["model_state_dict"]
            )

        else:

            self.load_state_dict(
                checkpoint
            )

        self.eval()
    
    def save_weights(
        self,
        checkpoint_path: str | Path,
    ):

        torch.save(
            self.state_dict(),
            checkpoint_path,
        )