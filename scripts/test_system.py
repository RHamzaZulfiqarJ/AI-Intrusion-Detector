from src.mlops import ExperimentManager, SystemLogger

experiment = ExperimentManager()

with experiment.start_run("System Test"):

    SystemLogger.log()

print("Done")