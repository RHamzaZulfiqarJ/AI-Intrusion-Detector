from __future__ import annotations

import json
import pickle
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


class ArtifactManager:
    """
    Handles saving all project artifacts.

    Supported:
    - CSV
    - JSON
    - Pickle
    - Matplotlib Figures
    - Text files
    """

    def __init__(self, base_dir: str | Path = "artifacts"):

        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def create_directory(self, *parts: str) -> Path:

        directory = self.base_dir.joinpath(*parts)
        directory.mkdir(parents=True, exist_ok=True)

        return directory

    def load_pickle(
        self,
        filename: str,
        *subdirs: str,
    ):

        path = self.base_dir.joinpath(
            *subdirs,
            filename,
        )

        if not path.exists():

            raise FileNotFoundError(
                f"Artifact not found: {path}"
            )

        with open(path, "rb") as file:

            return pickle.load(file)
        
    def load_json(
        self,
        filename: str,
        *subdirs: str,
    ):

        path = self.base_dir.joinpath(
            *subdirs,
            filename,
        )

        if not path.exists():

            raise FileNotFoundError(
                f"Artifact not found: {path}"
            )

        with open(path, "r", encoding="utf-8") as file:

            return json.load(file)

    def save_csv(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        *subdirs: str,
        index: bool = False,
    ) -> Path:

        directory = self.create_directory(*subdirs)

        path = directory / filename

        dataframe.to_csv(path, index=index)

        return path

    def save_json(
        self,
        data: dict,
        filename: str,
        *subdirs: str,
    ) -> Path:

        directory = self.create_directory(*subdirs)

        path = directory / filename

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False,
            )

        return path

    def save_pickle(
        self,
        obj: Any,
        filename: str,
        *subdirs: str,
    ) -> Path:

        directory = self.create_directory(*subdirs)

        path = directory / filename

        with open(path, "wb") as f:
            pickle.dump(obj, f)

        return path

    def save_plot(
        self,
        figure: plt.Figure,
        filename: str,
        *subdirs: str,
        dpi: int = 300,
    ) -> Path:

        directory = self.create_directory(*subdirs)

        path = directory / filename

        figure.savefig(
            path,
            dpi=dpi,
            bbox_inches="tight",
        )

        plt.close(figure)

        return path

    def save_text(
        self,
        text: str,
        filename: str,
        *subdirs: str,
    ) -> Path:

        directory = self.create_directory(*subdirs)

        path = directory / filename

        path.write_text(text)

        return path