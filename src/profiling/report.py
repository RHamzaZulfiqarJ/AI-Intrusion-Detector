from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from pathlib import Path


@dataclass(slots=True)
class AnalysisResult:
    """
    Result returned by every profiling module.
    """

    name: str

    summary: dict

    artifacts: list[Path] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    success: bool = True