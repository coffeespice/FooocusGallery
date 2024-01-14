import os
import json


def load_env():
    config_file = 'config.json'

    if not os.path.exists(config_file):
        return

    with open(config_file, 'r') as file:
        json_config = json.load(file)

    for key, value in json_config.items():
        os.environ[key] = value


def outputs_directory():
    return os.environ.get('outputs_directory')
