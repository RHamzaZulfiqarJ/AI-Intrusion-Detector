from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.scaler import DatasetScaler
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

    scaler = DatasetScaler()

    train_df = scaler.fit_transform(train_df)

    validation_df = scaler.transform(validation_df)

    test_df = scaler.transform(test_df)

    print("=" * 60)

    print(train_df.head())

    print()

    print(train_df.shape)

    print(validation_df.shape)

    print(test_df.shape)


if __name__ == "__main__":
    main()