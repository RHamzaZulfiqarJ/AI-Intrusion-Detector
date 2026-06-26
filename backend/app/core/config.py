from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):

    APP_NAME: str = "SecureGen"

    API_VERSION: str = "1.0.0"

    MODEL_VERSION: str = "v1"

    MODEL_NAME: str = "SecureGen IDS"

    EMBEDDING_MODEL: str = "BAAI/bge-base-en-v1.5"

    GEMINI_MODEL: str = "gemini-2.5-flash"

    GEMINI_API_KEY: str = ""

    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    MODEL_PATH: str = "training/checkpoints/best_model.pth"

    SCALER_PATH: str = "artifacts/scalers/standard_scaler.pkl"

    ENCODER_PATH: str = "artifacts/encoders/label_encoder.pkl"

    FEATURE_SCHEMA: str = "artifacts/metadata/feature_columns.json"

    VECTOR_INDEX: str = "artifacts/vector_store/vector_index.faiss"

    EMBEDDINGS: str = "artifacts/embeddings/embeddings.npy"

    METADATA: str = "artifacts/embeddings/metadata.json"
    
    model_config = SettingsConfigDict(

        env_file=".env",

        case_sensitive=False,

        extra="ignore",   # Recommended

    )


settings = Settings()