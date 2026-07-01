from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime

import mlflow

from src.mlops.tracking import TrackingManager


class ExperimentManager:

    def __init__(self):

        self.tracking = TrackingManager()

    @contextmanager
    def start_run(
        self,
        run_name: str | None = None,
        nested: bool = False,
    ):

        if run_name is None:

            run_name = datetime.now().strftime(
                "Run_%Y%m%d_%H%M%S"
            )

        with mlflow.start_run(
            run_name=run_name,
            nested=nested,
        ) as run:

            yield run

    @staticmethod
    def active_run():

        return mlflow.active_run()

    @staticmethod
    def end_run():

        if mlflow.active_run():

            mlflow.end_run()