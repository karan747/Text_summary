import os
from box.exceptions import BoxValueError
import yaml
from Text_summary.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from pynvml import *

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_dirs:list, verbose=True):
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size_in_KB(path:Path) ->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def print_gpu_utilization():

    nvmlInit()

    handle = nvmlDeviceGetHandleByIndex(0)

    info = nvmlDeviceGetMemoryInfo(handle)

    print(f"GPU memory occupied: {info.used//1024**2} MB.")


def print_summary(result):

    print(f"Time: {result.metrics['train_runtime']:.2f}")

    print(f"Samples/second: {result.metrics['train_samples_per_second']:.2f}")

    print_gpu_utilization()