import torch

from src.training.metrics import Metrics


def main():

    labels = torch.tensor(
        [0, 1, 2, 2, 1, 0, 1, 2]
    )

    predictions = torch.tensor(
        [0, 1, 2, 1, 1, 0, 0, 2]
    )

    print("=" * 60)

    print(
        "Accuracy:",
        Metrics.accuracy(
            predictions,
            labels,
        ),
    )

    print(
        "Precision:",
        Metrics.precision(
            predictions,
            labels,
        ),
    )

    print(
        "Recall:",
        Metrics.recall(
            predictions,
            labels,
        ),
    )

    print(
        "F1:",
        Metrics.f1(
            predictions,
            labels,
        ),
    )

    print()

    print(
        Metrics.confusion(
            predictions,
            labels,
        )
    )


if __name__ == "__main__":
    main()