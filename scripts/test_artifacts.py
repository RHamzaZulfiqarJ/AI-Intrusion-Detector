from src.mlops import ArtifactLogger, ExperimentManager

experiment = ExperimentManager()

with experiment.start_run("Artifact Test"):

    ArtifactLogger.log_if_exists(
        "artifacts/evaluation",
        "artifacts/metadata",
        "artifacts/encoders",
        "artifacts/scalers",
    )

print("Done")