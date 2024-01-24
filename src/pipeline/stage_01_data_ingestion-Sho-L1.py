from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion"


class DataIngestionPipeline:

    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()


if __name__ == '__main__':
    try:
        logging.info(f'>>>>>stage {STAGE_NAME} started <<<<<<')
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(f'>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x===========x')

    except Exception as e:
        raise CustomException(e, sys)