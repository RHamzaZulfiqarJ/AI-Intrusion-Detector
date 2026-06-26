import numpy as np
import pandas as pd

from configs.settings import LABEL_COLUMN

def count_duplicates(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())

def missing_values(df: pd.DataFrame):

    return (
        df.isnull()
          .sum()
          .to_dict()
    )
    
def infinite_values(df: pd.DataFrame):

    numeric = df.select_dtypes(include=np.number)

    inf = np.isinf(numeric)

    return inf.sum().to_dict()

def memory_usage(df: pd.DataFrame):

    return (
        df.memory_usage(deep=True)
          .sum()
          / 1024 ** 2
    )

def constant_columns(df: pd.DataFrame):

    constants = []

    for col in df.columns:

        if df[col].nunique(dropna=False) == 1:
            constants.append(col)

    return constants

def class_distribution(df):

    return (
        df[LABEL_COLUMN]
        .value_counts()
        .to_dict()
    )
    
def dtypes(df):

    return (
        df.dtypes
          .astype(str)
          .to_dict()
    )