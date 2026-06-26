from __future__ import annotations

import time

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from backend.app.core.dependencies import get_ai_service
from backend.app.schemas.request import PredictionRequest
from backend.app.schemas.prediction import Prediction
from backend.app.schemas.response import APIResponse
from backend.app.services.inference_service import BackendInferenceService
from backend.app.utils.request_validator import RequestValidator
from backend.app.core.config import settings


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)

validator = RequestValidator()


@router.post(
    "",
    response_model=APIResponse,
)

def predict(

    request_http: Request,

    request: PredictionRequest,

    service: BackendInferenceService = Depends(
        get_ai_service
    ),
):

    validation = validator.validate(
        request.features
    )

    if not validation["valid"]:

        raise HTTPException(

            status_code=400,

            detail={

                "message": "Invalid feature schema.",

                "missing": validation["missing"],

                "extra": validation["extra"],

            },

        )

    start = time.perf_counter()

    report = service.predict(
        request.features
    )

    latency = (
        time.perf_counter() - start
    ) * 1000

    prediction = Prediction(

        attack_name=report.attack_name,

        confidence=report.confidence,

        severity=report.severity,

        executive_summary=report.executive_summary,

        technical_explanation=report.technical_explanation,

        prediction_reason=report.prediction_reason,

        mitre_attack=report.mitre_attack,

        indicators_of_compromise=report.indicators_of_compromise,

        business_impact=report.business_impact,

        mitigations=report.mitigations,

        references=report.references,

    )

    return APIResponse(

        request_id=request_http.state.request_id,

        latency_ms=round(

            latency,

            2,

        ),

        model_version=settings.MODEL_VERSION,

        prediction=prediction,

    )