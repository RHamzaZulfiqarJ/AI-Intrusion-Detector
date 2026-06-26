from __future__ import annotations

import pandas as pd


def get_label_column(df: pd.DataFrame) -> str:
    """
    Return the label column regardless of leading/trailing spaces.
    """

    for column in df.columns:
        if column.strip().lower() == "label":
            return column

    raise KeyError("Could not locate label column.")