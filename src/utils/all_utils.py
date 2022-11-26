import yaml
import os
import logging

def yaml_read(path_for_yamlfile: str) -> dict:
    with open(path_for_yamlfile) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_dir(directory_name: list):
    for dir_path in directory_name:
        os.makedirs(dir_path,exist_ok=True)
        logging.info(f"Creating directory at {dir_path}")

