from __future__ import annotations

from torch.utils.data import DataLoader

from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.scaler import DatasetScaler
from src.preprocessing.splitter import DatasetSplitter
from src.training.dataset import CICIDSDataset
from src.training.model import IntrusionDetectionModel
from src.training.trainer import Trainer
from src.utils.logger import logger

def main():

    logger.info("=" * 80)
    logger.info("Starting SecureGenAI Training Pipeline")
    logger.info("=" * 80)

    # ------------------------------------------------------------------
    # Load Dataset
    # ------------------------------------------------------------------

    loader = DatasetLoader()

    dataframe = loader.merge()

    # ------------------------------------------------------------------
    # Clean Dataset
    # ------------------------------------------------------------------

    cleaner = DatasetCleaner(dataframe)

    dataframe = cleaner.clean()

    # ------------------------------------------------------------------
    # Encode Labels
    # ------------------------------------------------------------------

    encoder = DatasetEncoder(dataframe)

    dataframe = encoder.fit_transform()

    # ------------------------------------------------------------------
    # Split Dataset
    # ------------------------------------------------------------------

    splitter = DatasetSplitter(dataframe)

    train_df, validation_df, test_df = splitter.split()


    # ------------------------------------------------------------------
    # Scale Features
    # ------------------------------------------------------------------

    scaler = DatasetScaler()

    train_df = scaler.fit_transform(train_df)

    validation_df = scaler.transform(validation_df)

    test_df = scaler.transform(test_df)

    # ------------------------------------------------------------------
    # Build PyTorch Dataset
    # ------------------------------------------------------------------

    train_dataset = CICIDSDataset(train_df)

    validation_dataset = CICIDSDataset(validation_df)

    # ------------------------------------------------------------------
    # DataLoaders
    # ------------------------------------------------------------------

    train_loader = DataLoader(
        train_dataset,
        batch_size=1024,
        shuffle=True,
        num_workers=4,
        pin_memory=True,
        persistent_workers=True,
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=1024,
        shuffle=False,
        num_workers=4,
        pin_memory=True,
        persistent_workers=True,
    )

    # ------------------------------------------------------------------
    # Model
    # ------------------------------------------------------------------

    model = IntrusionDetectionModel(
        input_dim=train_df.shape[1] - 1,
        num_classes=15,
    )

    # ------------------------------------------------------------------
    # Trainer
    # ------------------------------------------------------------------

    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        learning_rate=1e-3,
        epochs=20,
        train_df=train_df,
        validation_df=validation_df,
        test_df=test_df,
    )

    history = trainer.train()

    logger.info("Training Finished Successfully.")

    return history


if __name__ == "__main__":

    main()