from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pandas as pd

from src.core.artifact_manager import ArtifactManager
from src.profiling.report import AnalysisResult
from src.utils.logger import logger


class BaseAnalysis(ABC):

    analysis_name = "base"

    def __init__(
        self,
        dataframe: pd.DataFrame,
        artifact_manager: ArtifactManager,
    ):
        self.df = dataframe
        self.artifacts = artifact_manager

    def execute(self) -> AnalysisResult:
        """
        Executes the analysis with automatic logging.
        """

        self.log_start()

        result = self.run()

        self.log_end()

        return result

    @abstractmethod
    def run(self) -> AnalysisResult:
        """
        Implement the analysis logic.
        """
        ...

    def log_start(self):

        logger.info(
            f"Running {self.analysis_name} analysis..."
        )

    def log_end(self):

        logger.info(
            f"{self.analysis_name} analysis completed."
        )