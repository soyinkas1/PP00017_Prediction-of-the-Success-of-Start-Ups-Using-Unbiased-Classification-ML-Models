from src.logger import logging
from src.pipeline.stage_02_data_cleaning import DataCleaningPipeline
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = 'Data Ingestion'

try:
    logging.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = 'Data Cleaning and Merging'

try:
    logging.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
    data_cleaning = DataCleaningPipeline()
    data_cleaning.main()
    logging.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
except Exception as e:
    logging.exception(e)
    raise e

