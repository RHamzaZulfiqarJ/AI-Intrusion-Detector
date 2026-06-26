from torch.utils.data import DataLoader

from src.evaluation.evaluator import Evaluator
from src.preprocessing.cleaner import DatasetCleaner
from src.preprocessing.encoder import DatasetEncoder
from src.preprocessing.loader import DatasetLoader
from src.preprocessing.scaler import DatasetScaler
from src.preprocessing.splitter import DatasetSplitter
from src.training.dataset import CICIDSDataset
from src.training.model import IntrusionDetectionModel


def main():

    loader = DatasetLoader()
    df = loader.merge()

    cleaner = DatasetCleaner(df)
    df = cleaner.clean()

    encoder = DatasetEncoder(df)
    df = encoder.fit_transform()

    splitter = DatasetSplitter(df)

    _, _, test_df = splitter.split()

    scaler = DatasetScaler()

    scaler.fit_transform(df)

    test_df = scaler.transform(test_df)

    test_dataset = CICIDSDataset(test_df)

    test_loader = DataLoader(
        test_dataset,
        batch_size=1024,
        shuffle=False,
        num_workers=4,
    )

    model = IntrusionDetectionModel()

    evaluator = Evaluator(
        model=model,
        test_loader=test_loader,
        checkpoint_path="training/checkpoints/best_model.pth",
    )

    metrics = evaluator.evaluate()

    print(metrics)


if __name__ == "__main__":
    main()