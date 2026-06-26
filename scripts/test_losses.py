import torch

from src.training.losses import LossFactory


def main():

    outputs = torch.randn(32, 15)

    labels = torch.randint(
        0,
        15,
        (32,),
    )

    ce = LossFactory.cross_entropy()

    focal = LossFactory.focal_loss()

    print("=" * 60)

    print(
        "CrossEntropy:",
        ce(outputs, labels).item(),
    )

    print(
        "FocalLoss:",
        focal(outputs, labels).item(),
    )


if __name__ == "__main__":
    main()