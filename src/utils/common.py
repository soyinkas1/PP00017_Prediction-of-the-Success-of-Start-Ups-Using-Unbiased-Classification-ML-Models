# Import the required libraries
import re
import os
from src.logger import logging
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations


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

@ensure_annotations
def clean_tweet(tweet: str) -> str:
    """
    Parameters:
    ----------
    Tweet: String type of the tweet content

    Returns:
    ---------
    cleaned version of the string tweet

    """
    tweet = tweet.lower()  # Lowercasing all the letters
    tweet = re.sub("@[A-Za-z0-9_]+", "", tweet)  # Remove all the mentions
    tweet = re.sub("#[A-Za-z0-9_]+", "", tweet)  # Remove all the hashtags
    tweet = re.sub(r"http\S+", "", tweet)  # Remove the URL
    tweet = re.sub(r"www.\S+", "", tweet)  # Remove the URL
    tweet = re.sub('[()!?]', ' ', tweet)  # Remove punctuations
    tweet = re.sub('\[.*?\]', ' ', tweet)  # Remove punctuations
    tweet = re.sub("[^a-z0-9]", " ", tweet)  # Remove all non-alphanumeric characters

    return tweet

@ensure_annotations
def clean_dict(data: dict) -> dict:
    """
    Parameters:
    ----------
    data: Dictionary of the DataFrames with tweets to clean

    Returns:
    ---------
    Dictionary of DataFrame with clean tweets

    """

    for key, val in data.items():
        val.dropna(subset=['text'], inplace=True)  # Drop NAs
        data[key] = val  # Update dictionary

        new_string = []  # create list to store cleaned tweets
        for tweet in val['text']:
            tweet = clean_tweet(tweet)  # Clean tweets
            new_string.append(tweet)

        val['text'] = new_string  # update the dataframe with clean tweet
        data[key] = val
    return data

@ensure_annotations
def get_analysis(score):
    """
    Converts the polarity score to text analysis
    :param score:
    :return: textual sentiment (Negative, Neutral or Positive
    """
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
