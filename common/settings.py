import pathlib
import yaml


BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'config.yaml'
test_config_path = BASE_DIR / 'config' / 'tests.yaml'

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


def get_test_config(path):
    with open(path) as f:
        test_config = yaml.safe_load(f)
    return test_config


config = get_config(config_path)
test_config = get_test_config(test_config_path)
