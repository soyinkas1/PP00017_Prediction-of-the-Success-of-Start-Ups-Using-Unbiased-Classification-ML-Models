from src.config.configuration import ConfigurationManager
from src.components.data_cleaning import DataCleaning
from src.logger import logging
from src.exception import CustomException
import sys
from src.entity.config_entity import DataCleaningConfig

STAGE_NAME = "Data Cleaning Stage"

class DataCleaningPipeline:

    def __init__(self, config: DataCleaningConfig):
            self.cleaning_config = config

    def main(self):
        config = ConfigurationManager()
        data_cleaning_config = config.get_data_cleaning_config()
        data_cleaning = DataCleaning(config=data_cleaning_config)
        data_cleaning.clean_data()


if __name__ == '__main__':
    try:
        logging.info(f'>>>>>stage {STAGE_NAME} started <<<<<<')
        obj = DataCleaningPipeline()
        obj.main()
        logging.info(f'>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x===========x')

    except Exception as e:
        raise CustomException(e, sys)