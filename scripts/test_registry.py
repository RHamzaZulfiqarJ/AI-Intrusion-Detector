import torch

from src.mlops import ExperimentManager, ModelRegistry
from src.training.model import IntrusionDetectionModel

model = IntrusionDetectionModel(
    input_dim=70,
    num_classes=15,
)

example = torch.randn(1, 70)

experiment = ExperimentManager()

with experiment.start_run("Registry Test"):

    ModelRegistry.register(
        model=model,
        input_example=example,
    )

print("Done")