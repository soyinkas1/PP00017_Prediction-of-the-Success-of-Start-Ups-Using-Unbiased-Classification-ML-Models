import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.utils import imput_rank, ScraperTool, ScraperToolConfig
from src.logger import logging
import warnings
from src.components.data_cleaning import clean_data

# Scrape Twitter

# t_scraper = ScraperTool()
# t_scraper.scrape_twitter(df_rows=5, max_tweets=20)


# Scrape Facebook


# Sensitivity Analysis


# Enrich dataset

if __name__ == '__main__':
    clean_data()
    t_scraper = ScraperTool()
    t_scraper.scrape_twitter(df_rows=5, max_tweets=20)
