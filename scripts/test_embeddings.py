from src.rag.chunker import TextChunker
from src.rag.document_loader import DocumentLoader
from src.rag.embeddings import EmbeddingGenerator


def main():

    loader = DocumentLoader()

    documents = loader.load_documents()

    chunker = TextChunker(
        chunk_size=500,
        overlap=100,
    )

    chunks = chunker.chunk_documents(
        documents
    )

    generator = EmbeddingGenerator()

    embeddings = generator.generate(
        chunks
    )

    generator.save(
        chunks,
        embeddings,
    )

    print("=" * 60)

    print("Chunks:", len(chunks))

    print("Embedding Shape:")

    print(embeddings.shape)


if __name__ == "__main__":

    main()