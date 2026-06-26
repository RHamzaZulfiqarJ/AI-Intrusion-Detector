from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.core.artifact_manager import ArtifactManager
from src.utils.logger import logger


class DatasetScaler:

    def __init__(
        self,
        label_column: str = "Label",
    ):

        self.label_column = label_column

        self.scaler = StandardScaler()

        self.artifacts = ArtifactManager()
        
    def load(self):

        logger.info("Loading StandardScaler...")

        self.scaler = self.artifacts.load_pickle(
            "standard_scaler.pkl",
            "scalers",
        )

        logger.info("StandardScaler loaded successfully.")

    def fit_transform(
        self,
        train_df: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Fitting StandardScaler on training data...")

        features = train_df.drop(columns=[self.label_column])
        
        self.artifacts.save_json(
            {
                "feature_columns": features.columns.tolist()
            },
            "feature_columns.json",
            "metadata",
        )

        labels = train_df[self.label_column]

        scaled_features = self.scaler.fit_transform(features)

        scaled_df = pd.DataFrame(
            scaled_features,
            columns=features.columns,
            index=train_df.index,
        )

        scaled_df[self.label_column] = labels.values

        self.artifacts.save_pickle(
            self.scaler,
            "standard_scaler.pkl",
            "scalers",
        )

        logger.info("Training data scaled successfully.")

        return scaled_df

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("Scaling dataset...")

        if self.label_column in dataframe.columns:

            features = dataframe.drop(columns=[self.label_column])

            labels = dataframe[self.label_column]

        else:

            features = dataframe

            labels = None

        scaled = self.scaler.transform(features)

        scaled_df = pd.DataFrame(
            scaled,
            columns=features.columns,
            index=dataframe.index,
        )

        if labels is not None:

            scaled_df[self.label_column] = labels.values

        return scaled_df