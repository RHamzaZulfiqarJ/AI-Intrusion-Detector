from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split

from src.utils.logger import logger


class DatasetSplitter:

    def __init__(
        self,
        dataframe: pd.DataFrame,
        label_column: str = "Label",
        train_size: float = 0.70,
        validation_size: float = 0.15,
        test_size: float = 0.15,
        random_state: int = 42,
    ):

        if abs(train_size + validation_size + test_size - 1.0) > 1e-6:
            raise ValueError(
                "Train, validation and test sizes must sum to 1."
            )

        self.df = dataframe

        self.label_column = label_column

        self.train_size = train_size
        self.validation_size = validation_size
        self.test_size = test_size

        self.random_state = random_state

    def split(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:

        logger.info("Splitting dataset...")

        train_df, temp_df = train_test_split(
            self.df,
            train_size=self.train_size,
            stratify=self.df[self.label_column],
            random_state=self.random_state,
            shuffle=True,
        )

        validation_ratio = (
            self.validation_size
            / (self.validation_size + self.test_size)
        )

        validation_df, test_df = train_test_split(
            temp_df,
            train_size=validation_ratio,
            stratify=temp_df[self.label_column],
            random_state=self.random_state,
            shuffle=True,
        )

        logger.info(
            f"Train: {train_df.shape}"
        )

        logger.info(
            f"Validation: {validation_df.shape}"
        )

        logger.info(
            f"Test: {test_df.shape}"
        )

        return (
            train_df.reset_index(drop=True),
            validation_df.reset_index(drop=True),
            test_df.reset_index(drop=True),
        )