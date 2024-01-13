from src.config.configuration import ConfigurationManager
from src.components.data_enrichment import DataEnrich
from src.logger import logging
from src.exception import CustomException
import sys
from src.entity.config_entity import DataCleaningConfig

STAGE_NAME = "Data Enrichment"


class DataEnrichmentPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_scrapping_config = config.get_data_scrapping_config()
        data_cleaning_config = config.get_data_cleaning_config()
        data_enrich_config = config.get_data_enrich_config()
        data_enrich = DataEnrich(config=data_enrich_config, scrapping_config=data_scrapping_config,
                                 data_cleaning_config=data_cleaning_config)

        data_enrich.get_tweet_sentiment_analysis()
        data_enrich.enrich_dataset()


if __name__ == '__main__':
    try:
        logging.info(f'>>>>>stage {STAGE_NAME} started <<<<<<')
        obj = DataEnrichmentPipeline()
        obj.main()
        logging.info(f'>>>>>stage {STAGE_NAME} completed <<<<<<\n\n x===========x')

    except Exception as e:
        raise CustomException(e, sys)
