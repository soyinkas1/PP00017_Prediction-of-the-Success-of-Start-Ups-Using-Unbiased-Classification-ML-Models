# Import the required libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dataclasses import dataclass
import os
import sys
from src.components.data_ingestion import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations




# def imput_rank(df):
#     """
#     The missing rank will be imputed with the nominal value from the tail end of the dataset
#     param: df: dataframe with a rank column named "rank" having missing values
#     """
#     leng= len(df)
#     counter = pd.Series(range(1,len(df['rank'][df['rank'].isna()] )+1))
#     df['rank'].mask(df['rank'].isna(), [leng-counter], inplace=True)




def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Arg:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging\
                .info(f'created directory at: {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    Args:
    path (Path): path to json file
    data (dict): data to be saved in json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f'json file saved at: {path}')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """

    :param
        path (Path): path to json file

    :return:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f'json file loaded successfully from: {path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
        save binary file

    :param
        data (Any): data to be saved as binary
        path (Path: path to binary file
    :return:
    """
    joblib.dump(value=data, filename=path)
    logging.info(f'binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
        load binary data
    :param
    path (Path): path to binary file

    :return:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f'binary file loaded from: {path}')
    return  data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    :param
        path (Path: path of the file

    :return:
        str; size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'