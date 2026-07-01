from __future__ import annotations

from pathlib import Path

import mlflow


class ArtifactLogger:

    @staticmethod
    def log(path: str | Path):

        path = Path(path)

        if not path.exists():
            return

        if path.is_file():
            mlflow.log_artifact(str(path))
        else:
            mlflow.log_artifacts(str(path))

    @staticmethod
    def log_if_exists(*paths):

        for path in paths:
            ArtifactLogger.log(path)