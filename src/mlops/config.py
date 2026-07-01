from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MLFLOW_TRACKING_URI = (
    f"sqlite:///{(PROJECT_ROOT / 'mlflow.db').as_posix()}"
)

MLFLOW_ARTIFACTS = PROJECT_ROOT / "mlartifacts"

EXPERIMENT_NAME = "AI Intrusion Detection"

REGISTERED_MODEL_NAME = "IntrusionDetector"

DEFAULT_TAGS = {
    "project": "AI Intrusion Detection",
    "framework": "PyTorch",
    "mlflow_version": "3.14",
}