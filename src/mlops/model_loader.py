from __future__ import annotations

import mlflow.pytorch

from src.mlops.config import REGISTERED_MODEL_NAME


class ModelLoader:

    @staticmethod
    def load(alias: str = "champion"):

        from src.mlops.tracking import TrackingManager

        # Initialize tracking manager to configure tracking URI
        _ = TrackingManager()

        model_uri = f"models:/{REGISTERED_MODEL_NAME}@{alias}"

        return mlflow.pytorch.load_model(model_uri)