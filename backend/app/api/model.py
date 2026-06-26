from fastapi import APIRouter

from backend.app.core.dependencies import (
    get_ai_service,
)

from fastapi import Depends

from backend.app.services.inference_service import (
    BackendInferenceService,
)


router = APIRouter(

    prefix="/model",

    tags=["Model"],

)


@router.get("")
def model_information(

    service: BackendInferenceService = Depends(

        get_ai_service

    ),

):

    return {

        "status": "loaded",

        "model": "IntrusionDetectionModel",

        "llm": "Gemini",

        "vector_database": "FAISS",

        "embedding_model": "BAAI/bge-base-en-v1.5",

    }