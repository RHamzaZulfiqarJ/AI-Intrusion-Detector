from src.preprocessing.loader import DatasetLoader
from src.profiling.profiler import DatasetProfiler


def main():

    loader = DatasetLoader()

    df = loader.merge()

    profiler = DatasetProfiler(df)

    results = profiler.run()

    for result in results:

        print("=" * 60)
        print(result.name)
        print(result.summary)


if __name__ == "__main__":
    main()