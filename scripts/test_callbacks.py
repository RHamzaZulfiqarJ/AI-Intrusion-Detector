import torch
import torch.nn as nn

from src.training.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
)


def main():

    model = nn.Linear(10, 2)

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=1e-3,
    )

    checkpoint = ModelCheckpoint()

    early_stopping = EarlyStopping(
        patience=3,
    )

    validation_losses = [
        0.90,
        0.75,
        0.70,
        0.72,
        0.74,
        0.76,
        0.77,
    ]

    for epoch, loss in enumerate(
        validation_losses,
        start=1,
    ):

        checkpoint(
            epoch,
            loss,
            model,
            optimizer,
        )

        stop = early_stopping(loss)

        print(
            f"Epoch {epoch} | Loss: {loss:.3f} | Stop: {stop}"
        )

        if stop:

            print("Early stopping triggered.")

            break


if __name__ == "__main__":
    main()