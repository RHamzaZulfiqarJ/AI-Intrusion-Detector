from pathlib import Path
import json

import pandas as pd

from src.preprocessing.validation_report import ValidationReport

from src.preprocessing.validation_rules import (
    count_duplicates,
    missing_values,
    infinite_values,
    constant_columns,
    class_distribution,
    dtypes,
    memory_usage
)

from src.utils.logger import logger

from dataclasses import asdict

class DatasetValidator:

    def __init__(self, dataframe):

        self.df = dataframe
        
    def run(self):

        logger.info("Starting dataset validation...")

        report = ValidationReport(

            rows=len(self.df),

            columns=len(self.df.columns),

            duplicate_rows=count_duplicates(self.df),

            missing_values=missing_values(self.df),

            infinite_values=infinite_values(self.df),

            constant_columns=constant_columns(self.df),

            class_distribution=class_distribution(self.df),

            dtypes=dtypes(self.df),

            memory_usage_mb=memory_usage(self.df)
        )

        logger.info("Validation completed.")

        return report
    
    def export(self, report):

        output = Path("artifacts/metadata")

        output.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output / "dataset_profile.json",
            "w"
        ) as f:

            json.dump(
                asdict(report),
                f,
                indent=4
            )