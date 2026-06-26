import numpy as np

from src.rag.embeddings import EmbeddingGenerator
from src.rag.vector_store import VectorStore


def main():

    generator = EmbeddingGenerator()

    embeddings = generator.load_embeddings()

    store = VectorStore()

    store.build(
        embeddings
    )

    store.save()

    store.load()

    query = embeddings[0].reshape(1, -1)

    scores, indices = store.search(
        query
    )

    print("=" * 60)

    print("Scores")

    print(scores)

    print()

    print("Indices")

    print(indices)


if __name__ == "__main__":

    main()