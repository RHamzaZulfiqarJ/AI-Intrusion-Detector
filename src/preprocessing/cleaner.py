from __future__ import annotations

import numpy as np
import pandas as pd

from src.utils.logger import logger


class DatasetCleaner:

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe.copy()

    def strip_column_names(self) -> None:
        """
        Remove leading and trailing whitespace from column names.
        """

        self.df.columns = self.df.columns.str.strip()

    def normalize_labels(self) -> None:
        """
        Normalize corrupted label names.
        """

        self.df["Label"] = (
            self.df["Label"]
            .astype(str)
            .str.replace("�", "-", regex=False)
            .str.strip()
        )

    def replace_infinite_values(self) -> None:
        """
        Replace positive and negative infinity with NaN.
        """

        self.df.replace(
            [np.inf, -np.inf],
            np.nan,
            inplace=True,
        )

    def handle_missing_values(self) -> None:
        """
        Remove rows containing missing values.
        """

        before = len(self.df)

        self.df.dropna(inplace=True)

        removed = before - len(self.df)

        logger.info(
            f"Removed {removed} rows containing missing values."
        )

    def remove_constant_features(self) -> None:
        """
        Remove constant columns.
        """

        constant_columns = [
            column
            for column in self.df.columns
            if self.df[column].nunique(dropna=False) == 1
        ]

        if constant_columns:

            self.df.drop(
                columns=constant_columns,
                inplace=True,
            )

            logger.info(
                f"Removed {len(constant_columns)} constant features."
            )

    def remove_duplicate_rows(self) -> None:
        """
        Remove duplicate rows.
        """

        before = len(self.df)

        self.df.drop_duplicates(
            inplace=True,
            ignore_index=True,
        )

        removed = before - len(self.df)

        logger.info(
            f"Removed {removed} duplicate rows."
        )

    def clean(self) -> pd.DataFrame:

        logger.info(
            "Starting dataset cleaning..."
        )

        self.strip_column_names()

        self.normalize_labels()

        self.replace_infinite_values()

        self.handle_missing_values()

        self.remove_constant_features()

        self.remove_duplicate_rows()

        logger.info(
            "Dataset cleaning completed."
        )

        return self.df