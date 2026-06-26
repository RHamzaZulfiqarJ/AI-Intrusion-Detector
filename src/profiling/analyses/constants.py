from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult


class ConstantFeatureAnalysis(BaseAnalysis):

    analysis_name = "constant_features"

    def run(self) -> AnalysisResult:

        constant_columns = []

        for column in self.df.columns:

            if self.df[column].nunique(dropna=False) == 1:
                constant_columns.append(column)

        constants_df = pd.DataFrame(
            {
                "Feature": constant_columns
            }
        )

        csv_path = self.artifacts.save_csv(
            constants_df,
            "constant_features.csv",
            "profiles",
            "constants",
            index=False,
        )

        json_path = self.artifacts.save_json(
            {
                "constant_features": constant_columns
            },
            "constant_features.json",
            "profiles",
            "constants",
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        if constant_columns:

            ax.bar(
                range(len(constant_columns)),
                [1] * len(constant_columns),
            )

            ax.set_xticks(range(len(constant_columns)))
            ax.set_xticklabels(
                constant_columns,
                rotation=45,
                ha="right",
            )

            ax.set_title("Constant Features")
            ax.set_ylabel("Constant")

        plot_path = self.artifacts.save_plot(
            fig,
            "constant_features.png",
            "profiles",
            "constants",
        )

        recommendations = []

        if constant_columns:

            recommendations.append(
                "Remove constant features before model training."
            )

        return AnalysisResult(
            name=self.analysis_name,
            summary={
                "constant_features": len(constant_columns),
            },
            artifacts=[
                csv_path,
                json_path,
                plot_path,
            ],
            recommendations=recommendations,
        )