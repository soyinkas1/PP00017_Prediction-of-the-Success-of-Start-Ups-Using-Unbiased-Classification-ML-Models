# Import the required libraries
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataCleaningConfig, 

# Import Data Cleaning and Wrangling Libraries
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import ydata_profiling

# Import Visualisation Libraries
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.express as px


# Import NLP Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Import Machine Learning Classifiers models Libraries
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

# Import evaluations modules
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import RocCurveDisplay


# Import other needed achine Learning Libraries
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder,MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB



class DataTransformation:
    """"
    This class is transform and carry out feature engineering to produce the final dataset for modelling
    """
    def __init__(self, config: DataTransformatonConfig, clean_data_config: DataCleaningConfig):
        self.scrapping_config = config
        self.clean_data_config = clean_data_config

    logging.info("Data scrapper configuration done......")

    def data_transformation(self):
    # Feature Engineering

    # We will derive features from the date based columns as follows:

    # per_exp_at_coy_start = founded_on - completed_on (This the experience of the personnel at founding date of company)
    # Degree Lenght = completed_on - started_on
    # Employee_count_min & Employee_count_max = Employee_count.split('-')
    # We will drop the following columns

    # state_code_o
    # postal_code_p
    # closed_on
    # completed_on
    # started_on
    # Finally we will rearrange the features as Index -> Numerical -> Categorical -> Text -> Target/Label