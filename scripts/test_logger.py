from src.mlops import ExperimentManager, MLflowLogger

experiment = ExperimentManager()

with experiment.start_run("Logger Test"):

    MLflowLogger.log_params({
        "learning_rate": 0.001,
        "batch_size": 1024,
    })

    MLflowLogger.log_metrics({
        "accuracy": 0.98,
        "loss": 0.02,
    })

    MLflowLogger.log_tags({
        "framework": "PyTorch",
        "stage": "testing",
    })

print("Done")