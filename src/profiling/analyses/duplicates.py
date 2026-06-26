from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult
from src.utils.dataframe_utils import get_label_column


class DuplicateAnalysis(BaseAnalysis):

    analysis_name = "duplicates"

    def run(self) -> AnalysisResult:

        label_column = get_label_column(self.df)

        duplicate_mask = self.df.duplicated()

        duplicate_rows = self.df[duplicate_mask]

        total_duplicates = int(duplicate_mask.sum())

        duplicate_percentage = round(
            (total_duplicates / len(self.df)) * 100,
            4,
        )

        if duplicate_rows.empty:

            duplicate_summary = pd.DataFrame(
                columns=[
                    "Class",
                    "Duplicate Count",
                    "Percentage",
                ]
            )

        else:

            duplicate_summary = (
                duplicate_rows[label_column]
                .value_counts()
                .rename("Duplicate Count")
                .to_frame()
            )

            duplicate_summary["Percentage"] = (
                duplicate_summary["Duplicate Count"]
                / total_duplicates
                * 100
            ).round(4)

            duplicate_summary.index.name = "Class"

        csv_path = self.artifacts.save_csv(
            duplicate_summary,
            "duplicates.csv",
            "profiles",
            "duplicates",
            index=True,
        )

        json_path = self.artifacts.save_json(
            duplicate_summary.to_dict(orient="index"),
            "duplicates.json",
            "profiles",
            "duplicates",
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        if not duplicate_summary.empty:

            ax.bar(
                duplicate_summary.index.astype(str),
                duplicate_summary["Duplicate Count"],
            )

            ax.set_title("Duplicate Records per Class")
            ax.set_xlabel("Class")
            ax.set_ylabel("Duplicate Count")

            plt.xticks(
                rotation=45,
                ha="right",
            )

        plot_path = self.artifacts.save_plot(
            fig,
            "duplicates.png",
            "profiles",
            "duplicates",
        )

        recommendations = []

        if total_duplicates > 0:

            recommendations.append(
                "Investigate duplicate records before removing them."
            )

        return AnalysisResult(
            name=self.analysis_name,
            summary={
                "total_duplicates": total_duplicates,
                "duplicate_percentage": duplicate_percentage,
                "affected_classes": len(duplicate_summary),
            },
            artifacts=[
                csv_path,
                json_path,
                plot_path,
            ],
            recommendations=recommendations,
        )