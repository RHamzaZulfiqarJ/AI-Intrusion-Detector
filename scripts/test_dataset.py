from torch.utils.data import DataLoader

from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.scaler import DatasetScaler
from src.preprocessing.splitter import DatasetSplitter
from src.training.dataset import CICIDSDataset

def main():

    loader = DatasetLoader()
    df = loader.merge()

    cleaner = DatasetCleaner(df)
    df = cleaner.clean()

    encoder = DatasetEncoder(df)
    df = encoder.fit_transform()

    splitter = DatasetSplitter(df)

    train_df, validation_df, test_df = splitter.split()

    scaler = DatasetScaler()

    train_df = scaler.fit_transform(train_df)
    validation_df = scaler.transform(validation_df)
    test_df = scaler.transform(test_df)

    train_dataset = CICIDSDataset(train_df)
    validation_dataset = CICIDSDataset(validation_df)
    test_dataset = CICIDSDataset(test_df)

    train_loader = DataLoader(
        train_dataset,
        batch_size=1024,
        shuffle=True,
        num_workers=4,
        pin_memory=True,
    )

    batch_features, batch_labels = next(iter(train_loader))

    print("=" * 60)

    print(batch_features.shape)

    print(batch_labels.shape)

    print(batch_labels[:10])


if __name__ == "__main__":
    main()