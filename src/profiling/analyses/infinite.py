from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult


class InfiniteAnalysis(BaseAnalysis):

    analysis_name = "infinite"

    def run(self) -> AnalysisResult:

        numeric_df = self.df.select_dtypes(include=np.number)

        infinite_counts = (
            pd.DataFrame(
                np.isinf(numeric_df),
                columns=numeric_df.columns,
            )
            .sum()
        )

        infinite_counts = infinite_counts[infinite_counts > 0]

        infinite_df = (
            infinite_counts
            .rename("Infinite Values")
            .to_frame()
        )

        csv_path = self.artifacts.save_csv(
            infinite_df,
            "infinite.csv",
            "profiles",
            "infinite",
        )

        json_path = self.artifacts.save_json(
            infinite_df.to_dict(orient="index"),
            "infinite.json",
            "profiles",
            "infinite",
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        if not infinite_df.empty:

            ax.bar(
                infinite_df.index,
                infinite_df["Infinite Values"],
            )

            ax.set_title("Infinite Values")
            ax.set_xlabel("Features")
            ax.set_ylabel("Count")

            plt.xticks(
                rotation=45,
                ha="right",
            )

        plot_path = self.artifacts.save_plot(
            fig,
            "infinite_values.png",
            "profiles",
            "infinite",
        )

        recommendations = []

        if not infinite_df.empty:
            recommendations.append(
                "Replace infinite values with NaN before handling missing values."
            )

        return AnalysisResult(
            name=self.analysis_name,
            summary={
                "total_infinite": int(
                    infinite_df["Infinite Values"].sum()
                ),
                "affected_columns": int(
                    len(infinite_df)
                ),
            },
            artifacts=[
                csv_path,
                json_path,
                plot_path,
            ],
            recommendations=recommendations,
        )