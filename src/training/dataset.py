from __future__ import annotations

import pandas as pd
import torch
from torch.utils.data import Dataset


class CICIDSDataset(Dataset):
    """
    PyTorch Dataset for CICIDS2017.
    """

    def __init__(
        self,
        dataframe: pd.DataFrame,
        label_column: str = "Label",
    ):

        self.features = torch.tensor(
            dataframe.drop(columns=[label_column]).values,
            dtype=torch.float32,
        )

        self.labels = torch.tensor(
            dataframe[label_column].values,
            dtype=torch.long,
        )

    def __len__(self) -> int:

        return len(self.labels)

    def __getitem__(self, index):

        return (
            self.features[index],
            self.labels[index],
        )