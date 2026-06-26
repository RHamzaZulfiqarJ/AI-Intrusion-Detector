from __future__ import annotations

from dataclasses import asdict

import pandas as pd

from src.core.artifact_manager import ArtifactManager
from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult


class OverviewAnalysis(BaseAnalysis):

    analysis_name = "overview"

    def __init__(
        self,
        dataframe: pd.DataFrame,
        artifact_manager: ArtifactManager,
    ):
        super().__init__(dataframe, artifact_manager)

    def run(self) -> AnalysisResult:

        rows = len(self.df)
        columns = len(self.df.columns)

        memory_mb = float(
            round(
                self.df.memory_usage(deep=True).sum() / (1024 ** 2),
                2,
            )
        )

        duplicates = int(self.df.duplicated().sum())

        missing_values = int(self.df.isnull().sum().sum())

        classes = int(
            self.df["Label"].nunique()
        )

        summary = {
            "rows": rows,
            "columns": columns,
            "memory_mb": round(memory_mb, 2),
            "duplicate_rows": duplicates,
            "missing_values": missing_values,
            "number_of_classes": classes,
        }

        csv = pd.DataFrame(
            [summary]
        )

        csv_path = self.artifacts.save_csv(
            csv,
            "overview.csv",
            "profiles",
            "overview"
        )

        json_path = self.artifacts.save_json(
            summary,
            "overview.json",
            "profiles",
            "overview"
        )

        result = AnalysisResult(
            name=self.analysis_name,
            summary=summary,
            artifacts=[csv_path, json_path],
        )

        return result