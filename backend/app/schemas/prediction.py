from __future__ import annotations

from pydantic import BaseModel

from src.llm.schemas import (
    Indicator,
    Mitigation,
    MitreTechnique,
    Reference,
)


class Prediction(BaseModel):

    attack_name: str

    confidence: float

    severity: str

    executive_summary: str

    technical_explanation: str

    prediction_reason: str

    mitre_attack: list[MitreTechnique]

    indicators_of_compromise: list[Indicator]

    business_impact: list[str]

    mitigations: list[Mitigation]

    references: list[Reference]