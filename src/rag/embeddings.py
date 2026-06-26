from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from src.rag.chunker import Chunk
from src.utils.logger import logger


class EmbeddingGenerator:

    def __init__(
        self,
        model_name: str = "BAAI/bge-base-en-v1.5",
        output_dir: str = "artifacts/embeddings",
    ):

        logger.info(
            f"Loading embedding model: {model_name}"
        )

        self.model = SentenceTransformer(
            model_name
        )

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        chunks: list[Chunk],
        batch_size: int = 64,
    ):

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks..."
        )

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        logger.info(
            "Embeddings generated successfully."
        )

        return embeddings

    def save(
        self,
        chunks: list[Chunk],
        embeddings: np.ndarray,
    ):

        np.save(
            self.output_dir / "embeddings.npy",
            embeddings,
        )

        metadata = []

        for chunk in chunks:

            metadata.append(
                {
                    "id": chunk.id,

                    "category": chunk.category,

                    "filename": chunk.filename,

                    "source": chunk.source,

                    "extension": chunk.extension,

                    "start": chunk.start,

                    "end": chunk.end,

                    "length": chunk.length,

                    "text": chunk.text,
                }
            )
            
        with open(
            self.output_dir / "metadata.json",
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
                ensure_ascii=False,
            )

        logger.info(
            "Embeddings saved successfully."
        )

    def load_embeddings(self):

        return np.load(
            self.output_dir / "embeddings.npy"
        )

    def load_metadata(self):

        with open(
            self.output_dir / "metadata.json",
            encoding="utf-8",
        ) as file:

            return json.load(file)