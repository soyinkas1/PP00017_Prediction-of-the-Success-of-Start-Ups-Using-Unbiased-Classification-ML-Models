# Import the required libraries
import re
import os
import pandas as pd
from src.logger import logging
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score, GridSearchCV
from src.exception import CustomException
import sys
import dill
from azure.storage.blob import BlobServiceClient

def download_blob_to_df(storage_name, storage_key, container_name, blob_name, chunksize,low_memory=True, nrows=None):

    try:
        blob_service_client = BlobServiceClient(
            account_url=f'https://{storage_name}.blob.core.windows.net',
            credential=storage_key
        )
       
        blob_client = blob_service_client.get_blob_client(container_name, blob=blob_name)
        blob_data = blob_client.download_blob()
        df = pd.read_csv(blob_data, chunksize=chunksize, low_memory=low_memory, nrows=nrows)
        return pd.concat(df)

    except Exception as e:
        raise CustomException(e, sys)

def upload_dataframe_to_blob(storage_name, storage_key, container_name, df, folder_file_name):

    try:
        blob_service_client = BlobServiceClient(
            account_url=f'https://{storage_name}.blob.core.windows.net',
            credential=storage_key
        )
        # Convert DataFrame to CSV string
        csv_data = df.to_csv(index=False)

        # Get blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f"{folder_file_name}")

        # Upload CSV data to blob
        blob_client.upload_blob(csv_data, overwrite=True)
    
    except Exception as e:
        raise CustomException(e, sys)




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
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove all punctuations
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
def get_analysis(score: int):
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
    
@ensure_annotations
def save_object(file_path: str | os.PathLike, obj):
    """
    Saves the object as a pickle file on the file_path provided
    
    """
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as file_obj:
        dill.dump(obj, file_obj)


@ensure_annotations
def load_object(file_path: str | os.PathLike):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
        

@ensure_annotations    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        """
        This method fits and score the models provided while doing a gridsearch cross
        validation using the parameter grid provided
        
        input: X-train - Training data input features
             y_train - Training data label 
             X_test - Test data input features
             y_test - Test data labels
             models - ML model to experiment with
             param :dict - parameter settings to try as values.
             
        Returns: a dictionary of the a key values pair of model and score
        """ 
        def get_object(class_path):
            """
            get the class object from the string returned from YAML 
            """
            module_name, class_name = class_path.rsplit('.', 1)
            module = __import__(module_name, fromlist=[class_name])
            
            return getattr(module, class_name)()
        
        for model_name, class_path in models.items():
             models[model_name] = get_object(class_path)
                
        report = {}
     
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
                     
            gs = GridSearchCV(model, para, cv=3, verbose=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            test_model_score = model.score(X_test, y_test)

            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise e
    


def process_in_batches(X, y, batch_size, path):
    try:
        n_samples = X.shape[0]
        for start in range(0, n_samples, batch_size):
            end = min(start + batch_size, n_samples)
            X_batch = X[start:end]
            y_batch = y[start:end]
            
            # Process each batch
            process_batch(X_batch, y_batch, path)
    except MemoryError as e:
        raise CustomException(e, sys)

def process_batch(X_batch, y_batch, path):
    # batch processing
    X_batch_dense = X_batch.todense()  # Only if absolutely necessary
    batch_df = pd.concat([pd.DataFrame(X_batch_dense), y_batch.reset_index(drop=True)], axis=1)
    
    
    # Continue processing the batch
    batch_df.to_csv(path, index=False, mode='a')
    print(f'shape of batched processed dataset:{batch_df.shape}')

