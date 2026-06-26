from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader


def main():

    loader = DatasetLoader()

    df = loader.merge()

    cleaner = DatasetCleaner(df)

    cleaned_df = cleaner.clean()

    encoder = DatasetEncoder(cleaned_df)

    encoded_df = encoder.fit_transform()

    print("=" * 60)

    print(encoded_df.head())

    print()

    print(encoded_df["Label"].value_counts().sort_index())


if __name__ == "__main__":
    main()