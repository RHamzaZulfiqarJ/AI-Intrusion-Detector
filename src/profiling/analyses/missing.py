from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from src.core.artifact_manager import ArtifactManager
from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult


class MissingAnalysis(BaseAnalysis):

    analysis_name = "missing"

    def __init__(
        self,
        dataframe: pd.DataFrame,
        artifact_manager: ArtifactManager,
    ):
        super().__init__(dataframe, artifact_manager)

    def run(self) -> AnalysisResult:

        missing = self.df.isnull().sum()

        missing = missing[missing > 0]

        missing_df = (
            missing
            .rename("Missing Values")
            .to_frame()
        )

        missing_df["Percentage"] = (
            missing_df["Missing Values"]
            / len(self.df)
            * 100
        ).round(4)

        csv_path = self.artifacts.save_csv(
            missing_df,
            "missing.csv",
            "profiles",
            "missing",
        )

        json_path = self.artifacts.save_json(
            missing_df.to_dict(orient="index"),
            "missing.json",
            "profiles",
            "missing",
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        if not missing_df.empty:
            ax.bar(
                missing_df.index,
                missing_df["Missing Values"],
            )

            ax.set_title("Missing Values")
            ax.set_ylabel("Count")

            plt.xticks(rotation=45, ha="right")

        plot_path = self.artifacts.save_plot(
            fig,
            "missing_values.png",
            "profiles",
            "missing",
        )

        recommendations = []

        if not missing_df.empty:
            recommendations.append(
                "Handle missing values during preprocessing."
            )

        return AnalysisResult(
            name=self.analysis_name,
            summary={
                "total_missing": int(
                    missing_df["Missing Values"].sum()
                ),
                "affected_columns": len(missing_df),
            },
            artifacts=[
                csv_path,
                json_path,
                plot_path,
            ],
            recommendations=recommendations,
        )