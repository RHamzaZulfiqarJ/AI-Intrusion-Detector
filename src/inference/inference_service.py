from __future__ import annotations

import torch
import pandas as pd

from src.llm.explanation_engine import ExplanationEngine
from src.llm.schemas import DetectionContext
from src.preprocessing.scaler import DatasetScaler
from src.preprocessing.encoder import DatasetEncoder
from src.training.model import IntrusionDetectionModel
from src.core.artifact_manager import ArtifactManager


class InferenceService:

    def __init__(

        self,

        scaler: DatasetScaler,

        encoder: DatasetEncoder,

        model: IntrusionDetectionModel,

        explanation_engine: ExplanationEngine,

        device: str = "cpu",

    ):

        self.scaler = scaler

        self.encoder = encoder

        self.model = model

        self.engine = explanation_engine
        
        self.artifacts = ArtifactManager()

        metadata = self.artifacts.load_json(
            "feature_columns.json",
            "metadata",
        )

        self.feature_columns = metadata["feature_columns"]

        self.device = device

        self.model.to(device)

        self.model.eval()

    @torch.no_grad()

    def predict(

        self,

        flow_features: dict,

    ):

        dataframe = pd.DataFrame(
            [flow_features]
        )

        dataframe = dataframe.reindex(
            columns=self.feature_columns,
            fill_value=0,
        )

        scaled = self.scaler.transform(

            dataframe

        )

        tensor = torch.tensor(

            scaled.values,

            dtype=torch.float32,

        ).to(self.device)

        logits = self.model(

            tensor

        )

        probabilities = torch.softmax(

            logits,

            dim=1,

        )[0]

        confidence, prediction = torch.max(

            probabilities,

            dim=0,

        )

        class_name = self.encoder.inverse_transform(

            int(prediction)

        )

        probability_dict = {

            self.encoder.inverse_transform(i):

            float(probabilities[i])

            for i in range(

                len(probabilities)

            )

        }

        detection = DetectionContext(

            prediction=class_name,

            confidence=float(confidence),

            probabilities=probability_dict,

            flow_features=flow_features,

        )

        report = self.engine.generate_report(

            detection

        )

        return report