from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.splitter import DatasetSplitter


def main():

    loader = DatasetLoader()
    df = loader.merge()

    cleaner = DatasetCleaner(df)
    cleaned_df = cleaner.clean()

    encoder = DatasetEncoder(cleaned_df)
    encoded_df = encoder.fit_transform()

    splitter = DatasetSplitter(encoded_df)

    train_df, validation_df, test_df = splitter.split()

    print("=" * 60)

    print(f"Train: {train_df.shape}")
    print(f"Validation: {validation_df.shape}")
    print(f"Test: {test_df.shape}")

    print()

    print("Train Label Distribution")
    print(train_df["Label"].value_counts().sort_index())


if __name__ == "__main__":
    main()