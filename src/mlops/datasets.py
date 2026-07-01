from __future__ import annotations

import hashlib
from pathlib import Path

import mlflow
import pandas as pd


class DatasetLogger:

    @staticmethod
    def log(
        train_df: pd.DataFrame,
        validation_df: pd.DataFrame,
        test_df: pd.DataFrame,
    ):

        mlflow.log_params({
            "train_rows": len(train_df),
            "validation_rows": len(validation_df),
            "test_rows": len(test_df),
            "num_features": train_df.shape[1] - 1,
            "num_classes": train_df.iloc[:, -1].nunique(),
        })

        metadata = {
            "columns": train_df.columns.tolist(),
            "train_shape": train_df.shape,
            "validation_shape": validation_df.shape,
            "test_shape": test_df.shape,
        }

        mlflow.log_dict(
            metadata,
            "dataset_metadata.json",
        )

        checksum = hashlib.md5(
            str(train_df.shape).encode()
        ).hexdigest()

        mlflow.set_tag(
            "dataset_checksum",
            checksum,
        )