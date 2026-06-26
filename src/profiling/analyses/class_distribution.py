from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from src.profiling.base import BaseAnalysis
from src.profiling.report import AnalysisResult
from src.utils.dataframe_utils import get_label_column


class ClassDistributionAnalysis(BaseAnalysis):

    analysis_name = "class_distribution"

    def run(self) -> AnalysisResult:

        label_column = get_label_column(self.df)

        class_counts = (
            self.df[label_column]
            .value_counts()
            .sort_values(ascending=False)
        )

        class_distribution = (
            class_counts
            .rename("Count")
            .to_frame()
        )

        class_distribution["Percentage"] = (
            class_distribution["Count"]
            / len(self.df)
            * 100
        ).round(4)

        class_distribution.index.name = "Class"

        csv_path = self.artifacts.save_csv(
            class_distribution,
            "class_distribution.csv",
            "profiles",
            "class_distribution",
            index=True,
        )

        json_path = self.artifacts.save_json(
            class_distribution.to_dict(orient="index"),
            "class_distribution.json",
            "profiles",
            "class_distribution",
        )

        fig, ax = plt.subplots(figsize=(14, 7))

        ax.bar(
            class_distribution.index.astype(str),
            class_distribution["Count"],
        )

        ax.set_title("Class Distribution")
        ax.set_xlabel("Attack Class")
        ax.set_ylabel("Number of Samples")

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plot_path = self.artifacts.save_plot(
            fig,
            "class_distribution.png",
            "profiles",
            "class_distribution",
        )

        largest_class = class_distribution["Count"].idxmax()
        smallest_class = class_distribution["Count"].idxmin()

        recommendations = [
            "Dataset is highly imbalanced. Consider class weighting or focal loss for training."
        ]

        return AnalysisResult(
            name=self.analysis_name,
            summary={
                "number_of_classes": int(len(class_distribution)),
                "largest_class": str(largest_class),
                "largest_class_count": int(class_distribution["Count"].max()),
                "smallest_class": str(smallest_class),
                "smallest_class_count": int(class_distribution["Count"].min()),
            },
            artifacts=[
                csv_path,
                json_path,
                plot_path,
            ],
            recommendations=recommendations,
        )