from src.rag.chunker import TextChunker
from src.rag.document_loader import DocumentLoader


def main():

    loader = DocumentLoader()

    documents = loader.load_documents()

    chunker = TextChunker(
        chunk_size=300,
        overlap=50,
    )

    chunks = chunker.chunk_documents(
        documents
    )

    print("=" * 60)

    print(f"Chunks: {len(chunks)}")

    for chunk in chunks[:5]:

        print()

        print("ID:", chunk.id)

        print("Source:", chunk.source)

        print("Characters:", chunk.start, "-", chunk.end)

        print(chunk.text[:200])


if __name__ == "__main__":

    main()