from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.core.dependencies import set_ai_service
from backend.app.services.inference_service import BackendInferenceService

from src.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Loading AI components...")

    service = BackendInferenceService()

    service.load()

    set_ai_service(service)

    logger.info("AI components loaded successfully.")

    yield

    logger.info("Shutting down API...")