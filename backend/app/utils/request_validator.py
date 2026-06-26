from __future__ import annotations

from src.core.artifact_manager import ArtifactManager


class RequestValidator:

    def __init__(self):

        artifacts = ArtifactManager()

        metadata = artifacts.load_json(

            "feature_columns.json",

            "metadata",

        )

        self.expected = set(

            metadata["feature_columns"]

        )

    def validate(

        self,

        features: dict,

    ):

        received = set(

            features.keys()

        )

        missing = sorted(

            self.expected - received

        )

        extra = sorted(

            received - self.expected

        )

        return {

            "valid": len(missing) == 0,

            "missing": missing,

            "extra": extra,

        }