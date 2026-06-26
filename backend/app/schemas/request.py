from __future__ import annotations

from typing import Dict

from pydantic import BaseModel
from pydantic import Field


class PredictionRequest(BaseModel):

    features: Dict[str, float] = Field(

        ...,

        description="Dictionary of network flow features.",

    )