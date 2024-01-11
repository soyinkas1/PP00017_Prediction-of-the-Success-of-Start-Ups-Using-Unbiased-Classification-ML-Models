import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_cleaning import DataCleaning
import numpy as np
from src.logger import logging
import warnings
from src.entity.config_entity import DataCleaningConfig, DataIngestionConfig
from src.utils.common import ScraperTool, ScraperToolConfig


class DataEnrichment:
    def __init__(self):

    # Scrape Twitter
    def twitter_data_scrape(self, max_tweets=None):
        t_scraper = ScraperTool()
        t_scraper.scrape_twitter(df_rows=5, max_tweets=20)


# Scrape Facebook


# Sensitivity Analysis


# Enrich dataset

if __name__ == '__main__':
    clean_data()
    t_scraper = ScraperTool()
    t_scraper.scrape_twitter(df_rows=5, max_tweets=20)
