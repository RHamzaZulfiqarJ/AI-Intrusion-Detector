from pathlib import Path

# ===========================
# Project Paths
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
METADATA_DIR = DATA_DIR / "metadata"

MODEL_DIR = BASE_DIR / "models"
MLFLOW_DIR = BASE_DIR / "mlruns"

LOG_DIR = BASE_DIR / "training" / "logs"

# ===========================
# General Settings
# ===========================

RANDOM_STATE = 42
DEVICE = "cuda"

# ===========================
# Dataset
# ===========================

LABEL_COLUMN = " Label"