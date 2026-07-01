from __future__ import annotations

from src.inference.inference_service import InferenceService

from src.llm.explanation_engine import ExplanationEngine

from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.scaler import DatasetScaler

from src.utils.logger import logger


class BackendInferenceService:

    def __init__(self):

        self.service: InferenceService | None = None

    def load(self):

        logger.info(
            "Loading backend inference service..."
        )

        # -----------------------------
        # Load scaler
        # -----------------------------

        scaler = DatasetScaler()

        scaler.load()

        # -----------------------------
        # Load label encoder
        # -----------------------------

        encoder = DatasetEncoder()

        encoder.load()

        # -----------------------------
        # Load trained model
        # -----------------------------

        from src.mlops.model_loader import ModelLoader

        model = ModelLoader.load()
        model.eval()

        # -----------------------------
        # Load explanation engine
        # -----------------------------

        engine = ExplanationEngine()

        # -----------------------------
        # Build AI pipeline
        # -----------------------------

        self.service = InferenceService(

            scaler=scaler,

            encoder=encoder,

            model=model,

            explanation_engine=engine,

        )

        logger.info(
            "Backend inference service loaded."
        )

    def predict(
        self,
        flow: dict,
    ):

        if self.service is None:

            raise RuntimeError(
                "Inference service is not initialized."
            )

        return self.service.predict(flow)