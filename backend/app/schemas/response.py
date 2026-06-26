from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field

from backend.app.schemas.prediction import Prediction


class APIResponse(BaseModel):

    success: bool = True

    request_id: str

    timestamp: datetime = Field(

        default_factory=datetime.utcnow

    )

    latency_ms: float

    model_version: str

    prediction: Prediction