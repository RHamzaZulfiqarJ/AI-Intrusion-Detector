# scripts/debug_mlflow.py

import mlflow

from src.mlops.config import MLFLOW_TRACKING_URI

print("Config URI:", MLFLOW_TRACKING_URI)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

print("MLflow URI:", mlflow.get_tracking_uri())