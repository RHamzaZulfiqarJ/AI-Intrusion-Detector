import pandas as pd

from src.mlops import DatasetLogger, ExperimentManager

train = pd.DataFrame({
    "f1": [1, 2],
    "f2": [3, 4],
    "label": [0, 1],
})

val = train.copy()
test = train.copy()

experiment = ExperimentManager()

with experiment.start_run("Dataset Test"):
    DatasetLogger.log(train, val, test)

print("Done")