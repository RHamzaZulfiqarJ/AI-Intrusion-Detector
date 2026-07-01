from __future__ import annotations

import mlflow
import mlflow.pytorch
import torch

from src.mlops.config import REGISTERED_MODEL_NAME


class ModelRegistry:

    @staticmethod
    def register(
        model: torch.nn.Module,
        input_example: torch.Tensor,
    ):

        model_info = mlflow.pytorch.log_model(
            pytorch_model=model,
            name="model",
            input_example=input_example,
            serialization_format="pickle",
        )

        model_version = mlflow.register_model(
            model_uri=model_info.model_uri,
            name=REGISTERED_MODEL_NAME,
        )

        version = model_version.version

        from mlflow import MlflowClient

        client = MlflowClient()

        client.set_registered_model_alias(
            REGISTERED_MODEL_NAME,
            "champion",
            version,
        )

        return version