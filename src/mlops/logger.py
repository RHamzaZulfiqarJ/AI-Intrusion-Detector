from __future__ import annotations

from pathlib import Path

import mlflow


class MLflowLogger:

    @staticmethod
    def log_params(params: dict):
        mlflow.log_params(params)

    @staticmethod
    def log_metrics(metrics: dict, step: int | None = None):
        if step is None:
            mlflow.log_metrics(metrics)
        else:
            for key, value in metrics.items():
                mlflow.log_metric(key, value, step=step)

    @staticmethod
    def log_tags(tags: dict):
        mlflow.set_tags(tags)

    @staticmethod
    def log_artifact(path: str | Path):
        mlflow.log_artifact(str(path))

    @staticmethod
    def log_artifacts(path: str | Path):
        mlflow.log_artifacts(str(path))

    @staticmethod
    def log_dict(data: dict, artifact_file: str):
        mlflow.log_dict(data, artifact_file)

    @staticmethod
    def log_text(text: str, artifact_file: str):
        mlflow.log_text(text, artifact_file)