from src.utils.all_utils import yaml_read,create_dir
import argparse
import os
import logging
import pickle

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_directory = 'logs'
os.makedirs(log_directory,exist_ok=True)
logging.basicConfig(filename=os.path.join(log_directory,'running_log.log'),level=logging.INFO,format=logging_str,filemode='a')


def generate_data_pickle_file(config_path,params_path):
    config=yaml_read(config_path)
    params=yaml_read(params_path)
    artifacts=config['artifacts']
    artifacts_dir = artifacts['artifacts_dir']
    pickle_format_data_dir = artifacts['pickle_format_data_dir']
    img_pickle_file_name = artifacts['img_pickle_file_name']
    raw_local_dir_path = os.path.join(artifacts_dir,pickle_format_data_dir)
    create_dir(directory_name=[raw_local_dir_path])
    pickle_file = os.path.join(raw_local_dir_path,img_pickle_file_name)
    data_path = params['base']['data_path']
    actors = os.listdir(data_path)
    print(actors)




if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument('--config', "-c", default='D://FaceMatchApp//config//config.yaml')
    args.add_argument('--params', "-p", default='D://FaceMatchApp//params.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info("stage01 started")
        generate_data_pickle_file(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info("stage01 completed")
    except Exception as e:
        logging.exception(e)
        raise e
