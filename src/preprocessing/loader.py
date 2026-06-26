from pathlib import Path

import pandas as pd
from tqdm import tqdm

from configs.settings import RAW_DATA_DIR
from src.utils.logger import logger


class DatasetLoader:
    """
    Loads and merges all CICIDS2017 CSV files.
    """

    def __init__(self, dataset_path: Path = RAW_DATA_DIR):
        self.dataset_path = dataset_path

    def discover_files(self) -> list[Path]:
        csv_files = sorted(self.dataset_path.glob("*.csv"))

        if not csv_files:
            raise FileNotFoundError(
                f"No CSV files found in {self.dataset_path}"
            )

        logger.info(f"Discovered {len(csv_files)} CSV files.")

        return csv_files

    def load_single_file(self, file_path: Path) -> pd.DataFrame:
        logger.info(f"Loading {file_path.name}")

        df = pd.read_csv(file_path)

        logger.info(
            f"{file_path.name} -> Shape: {df.shape}"
        )

        return df

    def validate_schema(self, dataframes: list[pd.DataFrame]):

        reference_columns = list(dataframes[0].columns)

        for i, df in enumerate(dataframes[1:], start=2):

            if list(df.columns) != reference_columns:
                raise ValueError(
                    f"Schema mismatch in dataframe {i}"
                )

        logger.info("Schema validation passed.")

    def merge(self) -> pd.DataFrame:

        files = self.discover_files()

        dfs = []

        for file in tqdm(files, desc="Loading CSV Files"):
            dfs.append(
                self.load_single_file(file)
            )

        self.validate_schema(dfs)

        merged_df = pd.concat(
            dfs,
            ignore_index=True
        )
        
        merged_df.columns = (
            merged_df.columns
            .str.strip()
        )

        logger.info(
            f"Merged dataset shape: {merged_df.shape}"
        )

        return merged_df
    
    def load(self) -> pd.DataFrame:

        return self.merge()