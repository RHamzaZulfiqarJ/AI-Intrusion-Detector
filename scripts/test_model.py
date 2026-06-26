import torch

from src.training.model import IntrusionDetectionModel


def main():

    model = IntrusionDetectionModel()

    dummy_batch = torch.randn(1024, 70)

    output = model(dummy_batch)

    print("=" * 60)

    print(model)

    print()

    print(output.shape)


if __name__ == "__main__":
    main()