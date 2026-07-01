# ==========================================================
# Base Image
# ==========================================================

FROM python:3.12-slim

# ==========================================================
# Environment Variables
# ==========================================================

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_HTTP_TIMEOUT=300

# ==========================================================
# Working Directory
# ==========================================================

WORKDIR /app

# ==========================================================
# System Dependencies
# ==========================================================

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ==========================================================
# Install Python Dependencies
# ==========================================================

COPY requirements ./requirements

# Copy the lightweight, pre-compiled static uv binary (~8MB)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install CPU-only PyTorch (using uv parallel download from PyTorch CPU index only)
RUN uv pip install --system --no-cache torch --index-url https://download.pytorch.org/whl/cpu

# Install rest of requirements using uv parallel downloader
RUN uv pip install --system --no-cache -r requirements/docker.txt

# Install google-genai (added here to leverage Docker cache and avoid 2-hour rebuild)
RUN uv pip install --system --no-cache google-genai

# Pre-download the embedding model during build time so container startup is fast
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-base-en-v1.5')"

# ==========================================================
# Copy Project
# ==========================================================

COPY . .

# Patch MLflow database paths from Windows host absolute URIs to Linux container paths
RUN python scripts/patch_mlflow_db.py

# ==========================================================
# Expose FastAPI Port
# ==========================================================

EXPOSE 8000

# ==========================================================
# Start API
# ==========================================================

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]