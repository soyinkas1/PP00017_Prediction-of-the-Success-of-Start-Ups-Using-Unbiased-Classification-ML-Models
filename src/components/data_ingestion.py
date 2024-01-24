import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
#from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import warnings

warnings.filterwarnings("ignore")

# @dataclass
# class DataIngestionConfig:
#     """
#     This class defines all the inputs (configurations) required for DataIngestion class
#     """
#     acquistions_data_path: str = os.path.join('artifacts', 'acquisitions.csv')
#     cat_groups_data_path: str = os.path.join('artifacts', 'category_groups.csv')
#     degrees_data_path: str = os.path.join('artifacts', 'degrees.csv')
#     event_appearances_data_path: str = os.path.join('artifacts', 'event_appearances.csv')
#     events_data_path: str = os.path.join('artifacts', 'events.csv')
#     funding_rounds_data_path: str = os.path.join('artifacts', 'funding_rounds.csv')
#     funds_data_path: str = os.path.join('artifacts', 'funds.csv')
#     investments_partners_data_path: str = os.path.join('artifacts', 'investments_partners.csv')
#     investments_data_path: str = os.path.join('artifacts', 'investments.csv')
#     investors_data_path: str = os.path.join('artifacts', 'investors.csv')
#     ipos_data_path: str = os.path.join('artifacts', 'ipos.csv')
#     jobs_data_path: str = os.path.join('artifacts', 'jobs.csv')
#     org_parents_data_path: str = os.path.join('artifacts', 'org_parents.csv')
#     organization_descriptions_data_path: str = os.path.join('artifacts', 'organization_descriptions.csv')
#     organizations_data_path: str = os.path.join('artifacts', 'organizations.csv')
#     people_data_path: str = os.path.join('artifacts', 'people.csv')
#     people_descriptions_data_path: str = os.path.join('artifacts', 'people_descriptions.csv')


class DataIngestion:
    """
    Class object that defines the data ingestion stage of the project
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        """ The method to ingest data from data sources"""
        logging.info('Entered data ingestion method or component')
        chunk_size = 100000
        try:
            # Create the artifact folder/directory
            os.makedirs(os.path.dirname(self.ingestion_config.people_data_path), exist_ok=True)
            acq_dfs = pd.read_csv('data/acquisitions.csv', chunksize=chunk_size, low_memory=True)
            acq_df = pd.concat(acq_dfs)
            logging.info('Read the acquisitions dataset as dataframe')
            acq_df.to_csv(self.ingestion_config.acquistions_data_path, index=False)
            logging.info('Saved the acquisitions dataset in csv format')

            catg_dfs = pd.read_csv('data/category_groups.csv', chunksize=chunk_size, low_memory=True)
            catg_df = pd.concat(catg_dfs)
            logging.info('Read the category groups dataset as dataframe')
            catg_df.to_csv(self.ingestion_config.cat_groups_data_path, index=False)
            logging.info('Saved the category groups dataset in csv format')

            deg_dfs = pd.read_csv('data/degrees.csv', chunksize=chunk_size, low_memory=True)
            deg_df = pd.concat(deg_dfs)
            logging.info('Read the degrees dataset as dataframe')
            deg_df.to_csv(self.ingestion_config.degrees_data_path, index=False)
            logging.info('Saved the degrees dataset in csv format')

            event_app_dfs = pd.read_csv('data/event_appearances.csv', chunksize=chunk_size, low_memory=True)
            event_app_df = pd.concat(event_app_dfs)
            logging.info('Read the event appearances dataset as dataframe')
            event_app_df.to_csv(self.ingestion_config.event_appearances_data_path, index=False)
            logging.info('Saved the event appearances dataset in csv format')

            events_dfs = pd.read_csv('data/events.csv', chunksize=chunk_size, low_memory=True)
            events_df = pd.concat(events_dfs)
            logging.info('Read the events dataset as dataframe')
            events_df.to_csv(self.ingestion_config.events_data_path, index=False)
            logging.info('Saved the events dataset in csv format')

            funding_rounds_dfs = pd.read_csv('data/funding_rounds.csv', chunksize=chunk_size, low_memory=True)
            funding_rounds_df = pd.concat(funding_rounds_dfs)
            logging.info('Read the funding rounds dataset as dataframe')
            funding_rounds_df.to_csv(self.ingestion_config.funding_rounds_data_path, index=False)
            logging.info('Saved the funding rounds dataset in csv format')

            funds_dfs = pd.read_csv('data/funds.csv', chunksize=chunk_size, low_memory=True)
            funds_df = pd.concat(funds_dfs)
            logging.info('Read the funds dataset as dataframe')
            funds_df.to_csv(self.ingestion_config.funds_data_path, index=False)
            logging.info('Saved the funds dataset in csv format')

            inv_partn_dfs = pd.read_csv('data/investment_partners.csv', chunksize=chunk_size, low_memory=True)
            inv_partn_df = pd.concat(inv_partn_dfs)
            logging.info('Read the investment partners dataset as dataframe')
            inv_partn_df.to_csv(self.ingestion_config.investments_partners_data_path, index=False)
            logging.info('Saved the investment partners dataset in csv format')

            inv_dfs = pd.read_csv('data/investments.csv', chunksize=chunk_size, low_memory=True)
            inv_df = pd.concat(inv_dfs)
            logging.info('Read the investments dataset as dataframe')
            inv_df.to_csv(self.ingestion_config.investments_data_path, index=False)
            logging.info('Saved the investments dataset in csv format')

            investors_dfs = pd.read_csv('data/investors.csv', chunksize=chunk_size, low_memory=True)
            investors_df = pd.concat(investors_dfs)
            logging.info('Read the investors dataset as dataframe')
            investors_df.to_csv(self.ingestion_config.investors_data_path, index=False)
            logging.info('Saved the investors dataset in csv format')

            ipos_dfs = pd.read_csv('data/ipos.csv', chunksize=chunk_size, low_memory=True)
            ipos_df = pd.concat(ipos_dfs)
            logging.info('Read the ipos dataset as dataframe')
            ipos_df.to_csv(self.ingestion_config.ipos_data_path, index=False)
            logging.info('Saved the ipos dataset in parquet format')

            jobs_dfs = pd.read_csv('data/jobs.csv', chunksize=chunk_size, low_memory=True)
            jobs_df = pd.concat(jobs_dfs)
            logging.info('Read the jobs dataset as dataframe')
            jobs_df.to_csv(self.ingestion_config.jobs_data_path, index=False)
            logging.info('Saved the jobs dataset in csv format')

            org_parents_dfs = pd.read_csv('data/org_parents.csv', chunksize=chunk_size, low_memory=True)
            org_parents_df = pd.concat(org_parents_dfs)
            logging.info('Read the organisation parents dataset as dataframe')
            org_parents_df.to_csv(self.ingestion_config.org_parents_data_path, index=False)
            logging.info('Saved the organisation parents dataset in csv format')

            organization_descriptions_dfs = pd.read_csv('data/organization_descriptions.csv', chunksize=chunk_size, low_memory=True)
            organization_descriptions_df = pd.concat(organization_descriptions_dfs)
            logging.info('Read the organization_descriptions dataset as dataframe')
            organization_descriptions_df.to_csv(self.ingestion_config.organization_descriptions_data_path, index=False)
            logging.info('Saved the organization_descriptions dataset in csv format')

            organizations_dfs = pd.read_csv('data/organizations.csv', chunksize=chunk_size, low_memory=True)
            organizations_df = pd.concat(organizations_dfs)
            logging.info('Read the organizations dataset as dataframe')
            organizations_df.to_csv(self.ingestion_config.organizations_data_path, index=False)
            logging.info('Saved the organizations dataset in csv format')

            people_dfs = pd.read_csv('data/people.csv', chunksize=chunk_size, low_memory=True)
            people_df = pd.concat(people_dfs)
            logging.info('Read the people dataset as dataframe')
            people_df.to_csv(self.ingestion_config.people_data_path, index=False)
            logging.info('Saved the people dataset in csv format')

            people_descriptions_dfs = pd.read_csv('data/people_descriptions.csv', chunksize=chunk_size, low_memory=True)
            people_descriptions_df = pd.concat(people_descriptions_dfs)
            logging.info('Read the people_descriptions dataset as dataframe')
            people_descriptions_df.to_csv(self.ingestion_config.people_descriptions_data_path, index=False)
            logging.info('Saved the people_descriptions dataset in csv format')

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.acquistions_data_path,
                self.ingestion_config.cat_groups_data_path,
                self.ingestion_config.degrees_data_path,
                self.ingestion_config.event_appearances_data_path,
                self.ingestion_config.events_data_path,
                self.ingestion_config.funding_rounds_data_path,
                self.ingestion_config.funds_data_path,
                self.ingestion_config.investments_partners_data_path,
                self.ingestion_config.investments_data_path,
                self.ingestion_config.investors_data_path,
                self.ingestion_config.ipos_data_path,
                self.ingestion_config.jobs_data_path,
                self.ingestion_config.org_parents_data_path,
                self.ingestion_config.organization_descriptions_data_path,
                self.ingestion_config.organizations_data_path,
                self.ingestion_config.people_data_path,
                self.ingestion_config.people_descriptions_data_path

            )

        except Exception as e:
            raise CustomException(e, sys)

# if __name__ == '__main__':
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()



