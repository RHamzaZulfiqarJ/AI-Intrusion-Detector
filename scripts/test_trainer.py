from torch.utils.data import DataLoader

from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.scaler import DatasetScaler
from src.preprocessing.splitter import DatasetSplitter
from src.training.dataset import CICIDSDataset
from src.training.model import IntrusionDetectionModel
from src.training.trainer import Trainer


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

    train_dataset = CICIDSDataset(train_df)
    validation_dataset = CICIDSDataset(validation_df)

    train_loader = DataLoader(
        train_dataset,
        batch_size=1024,
        shuffle=True,
        num_workers=4,
        pin_memory=True,
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=1024,
        shuffle=False,
        num_workers=4,
        pin_memory=True,
    )

    model = IntrusionDetectionModel()

    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        learning_rate=1e-3,
        epochs=5,
    )

    trainer.train()


if __name__ == "__main__":
    main()