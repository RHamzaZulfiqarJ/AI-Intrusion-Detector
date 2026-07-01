from __future__ import annotations

from pathlib import Path

import mlflow
from mlflow.tracking import MlflowClient

from src.mlops.config import (
    DEFAULT_TAGS,
    EXPERIMENT_NAME,
    MLFLOW_ARTIFACTS,
    MLFLOW_TRACKING_URI,
)


class TrackingManager:
    """
    Configures MLflow tracking.

    Responsible only for configuring
    the tracking backend and experiment.
    """

    def __init__(self):

        Path(MLFLOW_ARTIFACTS).mkdir(
            parents=True,
            exist_ok=True,
        )

        mlflow.set_tracking_uri(
            MLFLOW_TRACKING_URI
        )

        self.client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

        experiment = self.client.get_experiment_by_name(
            EXPERIMENT_NAME
        )

        if experiment is None:

            artifact_uri = (
                MLFLOW_ARTIFACTS.resolve()
                .as_uri()
            )

            exp_id = self.client.create_experiment(
                name=EXPERIMENT_NAME,
                artifact_location=artifact_uri,
                tags=DEFAULT_TAGS,
            )
            # Use the returned ID so we don't rely on a second lookup
            self._created_experiment_id = exp_id

        mlflow.set_experiment(
            EXPERIMENT_NAME
        )

    @property
    def tracking_uri(self):

        return mlflow.get_tracking_uri()

    @property
    def experiment(self):

        exp = self.client.get_experiment_by_name(
            EXPERIMENT_NAME
        )
        if exp is None:
            artifact_uri = (
                MLFLOW_ARTIFACTS.resolve()
                .as_uri()
            )
            exp_id = self.client.create_experiment(
                name=EXPERIMENT_NAME,
                artifact_location=artifact_uri,
                tags=DEFAULT_TAGS,
            )
            # Use the experiment_id returned by create_experiment directly
            # to avoid a second get_experiment_by_name call returning None
            exp = self.client.get_experiment(exp_id)
        return exp

    @property
    def experiment_id(self):

        exp = self.experiment
        return exp.experiment_id if exp is not None else None