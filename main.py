from src.logger import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_cleaning import DataCleaningPipeline
# from src.pipeline.stage_03_data_scrapping import DataScrappingPipeline
from src.pipeline import ModelTrainerPipeline


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

# STAGE_NAME = 'Data Scraping'

# try:
#     logging.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
#     data_scrapping = DataScrappingPipeline()
#     data_scrapping.main()
#     logging.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
# except Exception as e:
#     logging.exception(e)
#     raise e


# STAGE_NAME = 'Data Enrichment'

# try:
#     logging.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
#     data_enrich = DataEnrichmentPipeline()
#     data_enrich.main()
#     logging.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
# except Exception as e:
#     logging.exception(e)
#     raise e


# STAGE_NAME = 'Model Trainer'

# try:
#     logging.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
#     model_trainer = ModelTrainerPipeline()
#     model_trainer.main()
#     logging.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
# except Exception as e:
#     logging.exception(e)
#     raise e