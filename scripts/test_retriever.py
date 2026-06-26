from src.rag.retriever import Retriever


def main():

    retriever = Retriever()

    results = retriever.retrieve(

        query="Explain DoS Hulk attack.",

        category="DoS_Hulk",

        top_k=5,

    )

    print("=" * 60)

    for result in results:

        print()

        print("Score:", result.score)

        print("Category:", result.category)

        print("File:", result.filename)

        print("-" * 50)

        print(result.text[:350])


if __name__ == "__main__":

    main()