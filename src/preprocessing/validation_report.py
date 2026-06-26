from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ValidationReport:

    rows: int
    columns: int

    duplicate_rows: int

    missing_values: Dict[str, int]

    infinite_values: Dict[str, int]

    constant_columns: List[str]

    class_distribution: Dict[str, int]

    dtypes: Dict[str, str]

    memory_usage_mb: float

    warnings: List[str] = field(default_factory=list)

    passed: bool = True