from src.config.configuration import ConfigurationManager
from src.components.data_scrapping import DataScrapping
from src.logger import logging
from src.exception import CustomException
import sys
from src.entity.config_entity import DataCleaningConfig

STAGE_NAME = "Data Scraping"



class DataScrappingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_scrapping_config = config.get_data_scrapping_config()
        data_cleaning_config = config.get_data_cleaning_config()
        data_scrapping = DataScrapping(config=data_scrapping_config, clean_data_config=data_cleaning_config)
        data_scrapping.twitter_data_scrapping()


if __name__ == '__main__':
    try:
        logging.info(f'>>>>>stage {STAGE_NAME} started <<<<<<')
        obj = DataScrappingPipeline()
        obj.main()
        logging.info(f'>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x===========x')

    except Exception as e:
        raise CustomException(e, sys)
#