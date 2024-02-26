# Import Data Analysis Libraries
import pandas as pd
import numpy as np
import os
import dill
import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Import Machine Learning Classifiers models Libraries
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
import lightgbm as lgb
from xgboost import XGBClassifier


# Import evaluations modules
#from sklearn.metrics import plot_roc_curve
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import RocCurveDisplay


# Import other needed machine Learning Libraries
from sklearn.preprocessing import StandardScaler, OneHotEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score, GridSearchCV
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.pipeline import Pipeline

# import the internal classes and methods required
from entity.config_entity import DataTransformationConfig, ModelTrainerConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.common import save_object



class model_trainer:
    def __init__(self, config: ModelTrainerConfig):
        self.model_trainer_config = config
        # self.clean_data_config = clean_data_config
        

    def initiate_model_trainer(self, train_data_path, validation_path, test_data_path):

        # We will load the training, validation and test dataset

        train = pd.read_csv(self.model_trainer_config.train_data_path)
        val = pd.read_csv(self.model_trainer_config.validation_data_path)
        test = pd.read_csv(self.model_trainer_config.test_data_path)

