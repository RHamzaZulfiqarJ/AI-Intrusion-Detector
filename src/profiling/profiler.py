from __future__ import annotations

import pandas as pd

from src.core.artifact_manager import ArtifactManager
from src.profiling.analyses.overview import OverviewAnalysis
from src.profiling.analyses.missing import MissingAnalysis
from src.profiling.analyses.infinite import InfiniteAnalysis
from src.profiling.analyses.duplicates import DuplicateAnalysis
from src.profiling.analyses.constants import ConstantFeatureAnalysis
from src.profiling.analyses.class_distribution import ClassDistributionAnalysis

class DatasetProfiler:

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe

        self.artifact_manager = ArtifactManager()

        self.analyses = [
            OverviewAnalysis,
            MissingAnalysis,
            InfiniteAnalysis,
            DuplicateAnalysis,
            ConstantFeatureAnalysis,
            ClassDistributionAnalysis,
        ]

    def run(self):

        results = []

        for analysis in self.analyses:

            analyzer = analysis(
                self.df,
                self.artifact_manager,
            )

            results.append(
                analyzer.execute()
            )

        return results