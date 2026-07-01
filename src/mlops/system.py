from __future__ import annotations

import platform
import sys

import mlflow
import psutil
import torch


class SystemLogger:

    @staticmethod
    def log():

        mlflow.set_tags({

            "python_version": platform.python_version(),

            "platform": platform.platform(),

            "processor": platform.processor(),

            "cpu_count": psutil.cpu_count(logical=True),

            "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),

            "torch_version": torch.__version__,

            "cuda_available": torch.cuda.is_available(),

            "cuda_version": torch.version.cuda,

            "gpu_name": (
                torch.cuda.get_device_name(0)
                if torch.cuda.is_available()
                else "CPU"
            ),
        })