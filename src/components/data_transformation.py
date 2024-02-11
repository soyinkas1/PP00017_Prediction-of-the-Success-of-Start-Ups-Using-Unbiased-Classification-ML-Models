# Import the required libraries
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataCleaningConfig, 


class DataTransformation:
    """"
    This class is used for social media pages scrapping of the organization for enrichment of dataset
    """
    def __init__(self, config: DataScrappingConfig, clean_data_config: DataCleaningConfig):
        self.scrapping_config = config
        self.clean_data_config = clean_data_config

    logging.info("Data scrapper configuration done......")