from src.components import data_ingestion
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logging
from src.exception import CustomException
import sys
from src.entity.config_entity import DataCleaningConfig, DataTransformationConfig

STAGE_NAME = "Data Transformation"



class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transform_config = config.get_data_transform_config()
        data_cleaning_config = config.get_data_cleaning_config()
        data_ingestion_config = config.get_data_ingestion_config()
        data_transform = DataTransformation(config=data_transform_config, clean_data_config=data_cleaning_config, ingestion_config=data_ingestion_config)
        data_transform.data_transformation()


if __name__ == '__main__':
    try:
        logging.info(f'>>>>>stage {STAGE_NAME} started <<<<<<')
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f'>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x===========x')

    except Exception as e:
        raise CustomException(e, sys)
#