from __future__ import annotations

from pathlib import Path

import faiss
import numpy as np
import json

from src.utils.logger import logger


class VectorStore:

    def __init__(

        self,

        vector_store_dir: str = "artifacts/vector_store",

    ):

        self.vector_store_dir = Path(
            vector_store_dir
        )

        self.vector_store_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.index = None

    def build(
        self,
        embeddings: np.ndarray,
    ):

        logger.info(
            "Building FAISS index..."
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(
            embeddings.astype(
                np.float32
            )
        )

        logger.info(
            f"Indexed {self.index.ntotal} vectors."
        )

    def save(self):

        if self.index is None:

            raise RuntimeError(
                "No index available."
            )

        faiss.write_index(

            self.index,

            str(
                self.vector_store_dir /
                "vector_index.faiss"
            ),

        )

        logger.info(
            "FAISS index saved."
        )

    def load(self):

        self.index = faiss.read_index(

            str(
                self.vector_store_dir /
                "vector_index.faiss"
            )

        )

        logger.info(
            f"Loaded index with {self.index.ntotal} vectors."
        )

    def search(

        self,

        query_embedding: np.ndarray,

        top_k: int = 5,

    ):

        if self.index is None:

            raise RuntimeError(
                "Load index first."
            )

        scores, indices = self.index.search(

            query_embedding.astype(
                np.float32
            ),

            top_k,

        )

        return scores, indices
    
    def load_metadata(self):

        with open(

            "artifacts/embeddings/metadata.json",

            encoding="utf-8",

        ) as file:

            return json.load(file)