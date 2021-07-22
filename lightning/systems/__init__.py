from .baseline import BaselineSystem
from .meta import MetaSystem

SYSTEM = {
    "meta": MetaSystem,
    "baseline": BaselineSystem,
}

# def get_system(algorithm, preprocess_config, model_config, train_config, algorithm_config, log_dir, result_dir):
    # return SYSTEM[algorithm](preprocess_config, model_config, train_config, algorithm_config, log_dir, result_dir)
def get_system(algorithm):
    return SYSTEM[algorithm]
