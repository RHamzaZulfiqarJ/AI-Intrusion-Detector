from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sentence_transformers import SentenceTransformer

from src.rag.vector_store import VectorStore
from src.utils.logger import logger


@dataclass(slots=True)
class RetrievalResult:

    score: float

    category: str

    filename: str

    source: str

    text: str


class Retriever:

    def __init__(

        self,

        embedding_model: str = "BAAI/bge-base-en-v1.5",

    ):

        logger.info(
            f"Loading embedding model: {embedding_model}"
        )

        self.model = SentenceTransformer(
            embedding_model
        )

        self.store = VectorStore()

        self.store.load()

        self.metadata = self.store.load_metadata()

    def encode_query(
        self,
        query: str,
    ) -> np.ndarray:

        embedding = self.model.encode(

            [query],

            convert_to_numpy=True,

            normalize_embeddings=True,

        )

        return embedding.astype(np.float32)

    def retrieve(

        self,

        query: str,

        top_k: int = 5,

        category: str | None = None,

    ) -> list[RetrievalResult]:

        logger.info(
            f"Searching: {query}"
        )

        query_embedding = self.encode_query(
            query
        )

        scores, indices = self.store.search(

            query_embedding,

            top_k=top_k * 3 if category else top_k,

        )

        results = []

        for score, index in zip(

            scores[0],

            indices[0],

        ):

            item = self.metadata[index]

            if (

                category is not None

                and item["category"] != category

            ):

                continue

            results.append(

                RetrievalResult(

                    score=float(score),

                    category=item["category"],

                    filename=item["filename"],

                    source=item["source"],

                    text=item["text"],

                )

            )

            if len(results) >= top_k:

                break

        logger.info(
            f"Retrieved {len(results)} chunks."
        )

        return results