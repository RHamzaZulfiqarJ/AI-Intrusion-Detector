from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.loader import DatasetLoader


def main():

    loader = DatasetLoader()

    df = loader.merge()

    cleaner = DatasetCleaner(df)

    cleaned_df = cleaner.clean()

    print("=" * 60)

    print(cleaned_df.shape)

    print(cleaned_df.head())


if __name__ == "__main__":

    main()