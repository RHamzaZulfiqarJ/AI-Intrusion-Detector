from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# SQLite tracking database
MLFLOW_TRACKING_URI = f"sqlite:///{PROJECT_ROOT / 'mlflow.db'}"

EXPERIMENT_NAME = "AI Intrusion Detection"

REGISTERED_MODEL_NAME = "IntrusionDetector"

ARTIFACT_LOCATION = PROJECT_ROOT / "mlartifacts"