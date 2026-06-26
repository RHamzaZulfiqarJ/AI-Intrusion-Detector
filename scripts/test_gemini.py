from src.llm.gemini import GeminiLLM


def main():

    llm = GeminiLLM()

    print("=" * 60)

    print("Health Check:")

    print(llm.health_check())

    print()

    response = llm.generate(

        "Explain what a DoS Hulk attack is in three sentences."

    )

    print(response.response)

    print()

    print(f"Latency: {response.latency:.2f}s")


if __name__ == "__main__":

    main()