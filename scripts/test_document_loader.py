from src.rag.document_loader import DocumentLoader


def main():

    loader = DocumentLoader()

    documents = loader.load_documents()

    print("=" * 60)

    print(f"Documents: {len(documents)}")

    for document in documents:

        print()

        print(document.source)

        print(document.extension)

        print(document.text[:300])


if __name__ == "__main__":

    main()