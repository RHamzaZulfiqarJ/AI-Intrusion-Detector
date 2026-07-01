from src.mlops import ExperimentManager
from src.mlops import TrackingManager

tracking = TrackingManager()

print(tracking.tracking_uri)
print(tracking.experiment.name)

experiment = ExperimentManager()

with experiment.start_run() as run:

    print("Run ID:", run.info.run_id)

print("Done.")