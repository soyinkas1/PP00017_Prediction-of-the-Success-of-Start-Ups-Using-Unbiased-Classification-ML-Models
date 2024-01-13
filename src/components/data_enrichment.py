# Data Manipulation and cleaning Libraries
import os.path

import numpy as np
import re
import pandas as pd
from os import listdir
from os.path import isfile, join, isdir
from pathlib import Path
from src.utils.common import clean_dict, get_analysis
from src.entity.config_entity import DataEnrichConfig, DataScrappingConfig, DataCleaningConfig
from src.logger import logging
# NLP processing libraries
from textblob import TextBlob

class DataEnrich:

    def __init__(self, config: DataEnrichConfig, scrapping_config: DataScrappingConfig,
                 data_cleaning_config: DataCleaningConfig):
        self.enrich_config = config
        self.scrapping_config = scrapping_config
        self.data_clean_config = data_cleaning_config
    logging.info("Data enrichment configuration completed .....")

    # Sensitivity Analysis
    def get_tweet_sentiment_analysis(self):
        logging.info("Twitter sentiment analysis started......")
        # Step up path for file with tweets
        path = Path(self.scrapping_config.root_dir)
        # Add the file names to a list
        files = [f for f in listdir(path) if isfile(join(path, f))]
        # Read the all the dataset into a dictionary of DataFrames
        data = {}

        for i in range(0, len(files)+1):
            try:
                df = pd.read_csv(str(os.path.join(path, files[i])), usecols=self.enrich_config.column_to_load)
                data[f'{str(files[i]).split(".")[0]}'] = df

            except:
                pass

        # Clean the tweet datasets and save in a dictionary
        data_c = clean_dict(data)
        # CLean and reformat the followers and following columns
        for key, val in data_c.items():
            # Clean followers column
            for item in val[self.enrich_config.follower_data]:
                if str(item).find('K') != -1:
                    item = re.sub("[^0-9.]", "", item)  # format the K to '000'
                    item = re.sub('[,a-zA-Z]', "", item)  # remove all commas
                    item = float(item) * 1000
                    val[self.enrich_config.follower_data] = item
                    data_c[key] = val
                elif str(item).find('M') != -1:
                    item = re.sub("[^0-9.]", "", item)  # format the M to '000000'
                    item = re.sub('[,a-zA-Z]', "", item)  # remove all commas
                    item = float(item) * 1000000
                    val[self.enrich_config.follower_data] = item
                    data_c[key] = val
            # Clean following column
            for item in val[self.enrich_config.following_data]:
                if str(item).find('K') != -1:
                    item = re.sub("[^0-9.]", "", item)  # format the K to '000'
                    item = re.sub('[,a-zA-Z]', "", item)  # remove all commas
                    item = float(item) * 1000
                    val[self.enrich_config.following_data] = item
                    data_c[key] = val
                elif str(item).find('M') != -1:
                    item = re.sub("[^0-9.]", "", item)  # format the M to '000000'
                    item = re.sub('[,a-zA-Z]', "", item)  # remove all commas
                    item = float(item) * 1000000
                    val[self.enrich_config.following_data] = item
                    data_c[key] = val

            # Calculate the polarity and subjectivity
            try:
                val[self.enrich_config.polarity] = val[self.enrich_config.text].apply(
                    lambda x: TextBlob(x).sentiment.polarity)  # Calculates and add polarity columns
                val[self.enrich_config.subjectivity] = val[self.enrich_config.text].apply(
                    lambda x: TextBlob(x).sentiment.subjectivity) # Calculates and add subjectivity columns
                data_c[key] = val  # Update dictionary
            except:
                pass
        # Create single dataframe for all companies
        account = []
        followers = []
        following = []
        polarity = []
        subjectivity = []

        for key, val in data_c.items():
            for item in val[self.enrich_config.follower_data]:
                followers.append(item)
                break
            for item in val[self.enrich_config.following_data]:
                following.append(item)
                break
            for item in val[self.enrich_config.account]:
                account.append(item)
                break
            polarity.append(val[self.enrich_config.polarity].mean())
            subjectivity.append(val[self.enrich_config.subjectivity].mean())

        enrich_df = pd.DataFrame(list(zip(following, followers, polarity, subjectivity, account)),
                                 columns=self.enrich_config.enrich_data_columns)

        enrich_df[self.enrich_config.tweet_analysis] = enrich_df[self.enrich_config.polarity].apply(get_analysis)

        # Save the dataset
        enrich_df.to_csv(self.enrich_config.twitter_sentiment_local_data_file, index=False)
        logging.info("Twitter sentiment analysis completed......")
    # def get_facebook _sentiment_analysis(self):

    # def get_linkedin_sentiment_analysis(self):

    def enrich_dataset(self):
        logging.info("Data enrichment started......")
        # Read the Twitter sentiment analysis dataset
        twitter_sentiment_df = pd.read_csv(self.enrich_config.twitter_sentiment_local_data_file)
        # Read the unclean backbone dataset
        unclean_backbone_df = pd.read_csv(self.data_clean_config.unclean_backbone_local_data_file)
        # Merge the backbone dataset
        final_ds = pd.merge(twitter_sentiment_df, unclean_backbone_df,
                            on=self.scrapping_config.twitter_url, how='inner')
        # Read the Facebook sentiment analysis dataset

        # Merge the backbone dataset

        # Read the LinkedIn sentiment analysis dataset

        # Merge the backbone dataset

        # Save the enriched unclean backbone dataset
        final_ds.to_csv(self.enrich_config.enriched_backbone_local_data_file, index=False)
        logging.info("Data enrichment completed......")
