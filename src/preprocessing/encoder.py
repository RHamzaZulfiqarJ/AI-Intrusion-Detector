from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.core.artifact_manager import ArtifactManager
from src.utils.logger import logger


class DatasetEncoder:

    def __init__(
        self,
        dataframe: pd.DataFrame | None = None,
        label_column: str = "Label",
    ):
        self.df = dataframe.copy() if dataframe is not None else None

        self.label_column = label_column

        self.encoder = LabelEncoder()

        self.artifacts = ArtifactManager()
        
    def load(self):

        logger.info("Loading LabelEncoder...")

        self.encoder = self.artifacts.load_pickle(
            "label_encoder.pkl",
            "encoders",
        )

        logger.info("LabelEncoder loaded successfully.")

    def encode_labels(self) -> pd.DataFrame:
        """
        Encode the target labels into integer values.
        """

        logger.info("Encoding class labels...")

        self.df["Label"] = self.encoder.fit_transform(
            self.df["Label"]
        )

        logger.info("Label encoding completed.")

        return self.df

    def save_encoder(self) -> Path:
        """
        Save fitted LabelEncoder.
        """

        return self.artifacts.save_pickle(
            self.encoder,
            "label_encoder.pkl",
            "encoders",
        )

    def save_label_mapping(self) -> Path:
        """
        Save class-to-index mapping.
        """

        mapping = {
            class_name: int(index)
            for index, class_name in enumerate(
                self.encoder.classes_
            )
        }

        return self.artifacts.save_json(
            mapping,
            "label_mapping.json",
            "encoders",
        )

    def fit_transform(self) -> pd.DataFrame:

        encoded_df = self.encode_labels()

        self.save_encoder()

        self.save_label_mapping()

        return encoded_df
    
    def inverse_transform(

        self,

        label: int,

    ) -> str:

        return self.encoder.inverse_transform(

            [label]

        )[0]
        
    def inverse_transform(
        self,
        labels: int | list[int],
    ):

        if isinstance(labels, int):

            return self.encoder.inverse_transform(
                [labels]
            )[0]

        return self.encoder.inverse_transform(
            labels
        ).tolist()