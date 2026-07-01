from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from src.rag.retriever import RetrievalResult


@dataclass(slots=True)
class DetectionContext:
    """
    Output produced by the Intrusion Detection Model.
    """

    prediction: str

    confidence: float

    probabilities: dict[str, float]

    flow_features: dict[str, float]

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )


@dataclass(slots=True)
class PromptContext:
    """
    Information passed into the Prompt Builder.
    """

    detection: DetectionContext

    retrieved_chunks: list[RetrievalResult]


@dataclass(slots=True)
class LLMResponse:
    """
    Raw response returned by the LLM.
    """

    model_name: str

    prompt: str

    response: str

    latency: float


@dataclass(slots=True)
class SecurityReport:

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
    
@dataclass(slots=True)
class MitreTechnique:

    technique_id: str = ""

    technique_name: str = ""

    tactic: str = ""

    url: str = ""

@dataclass(slots=True)
class Indicator:

    indicator: str

    value: str

    description: str
    
@dataclass(slots=True)
class Mitigation:

    title: str

    description: str
    
@dataclass(slots=True)
class Reference:

    title: str

    url: str
    
