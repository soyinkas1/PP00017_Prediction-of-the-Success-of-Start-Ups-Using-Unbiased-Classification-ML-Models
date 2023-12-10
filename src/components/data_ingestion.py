import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
#from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    This class defines all the inputs (configurations) required for DataIngestion class
    """
    acquistions_data_path: str = os.path.join('artifacts', 'acquisitions.parquet')
    cat_groups_data_path: str = os.path.join('artifacts', 'category_groups.parquet')
    degrees_data_path: str = os.path.join('artifacts', 'degrees.parquet')
    event_appearances_data_path: str = os.path.join('artifacts', 'event_appearances.parquet')
    events_data_path: str = os.path.join('artifacts', 'events.parquet')
    funding_rounds_data_path: str = os.path.join('artifacts', 'funding_rounds.parquet')
    funds_data_path: str = os.path.join('artifacts', 'funds.parquet')
    investments_partners_data_path: str = os.path.join('artifacts', 'investments_partners.parquet')
    investments_data_path: str = os.path.join('artifacts', 'investments.parquet')
    investors_data_path: str = os.path.join('artifacts', 'investors.parquet')
    ipos_data_path: str = os.path.join('artifacts', 'ipos.parquet')
    jobs_data_path: str = os.path.join('artifacts', 'jobs.parquet')
    org_parents_data_path: str = os.path.join('artifacts', 'org_parents.parquet')
    organization_descriptions_data_path: str = os.path.join('artifacts', 'organization_descriptions.parquet')
    organizations_data_path: str = os.path.join('artifacts', 'organizations.parquet')
    people_data_path: str = os.path.join('artifacts', 'people.parquet')
    people_descriptions_data_path: str = os.path.join('artifacts', 'people_descriptions.parquet')


class DataIngestion:
    """
    Class object that defines the data ingestion stage of the project
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        """ The method to ingest data from data sources"""
        logging.info('Entered data ingestion method or component')
        try:
            # Create the artifact folder/directory
            os.makedirs(os.path.dirname(self.ingestion_config.people_data_path), exist_ok=True)
            acq_df = pd.read_csv('data/acquisitions.csv')
            logging.info('Read the acquisitions dataset as dataframe')
            acq_df.to_parquet(self.ingestion_config.acquistions_data_path)
            logging.info('Saved the acquisitions dataset in parquet format')

            catg_df = pd.read_csv('data/category_groups.csv')
            logging.info('Read the category groups dataset as dataframe')
            catg_df.to_parquet(self.ingestion_config.cat_groups_data_path)
            logging.info('Saved the category groups dataset in parquet format')

            deg_df = pd.read_csv('data/degrees.csv')
            logging.info('Read the degrees dataset as dataframe')
            deg_df.to_parquet(self.ingestion_config.degrees_data_path)
            logging.info('Saved the degrees dataset in parquet format')

            event_app_df = pd.read_csv('data/event_appearances.csv')
            logging.info('Read the event appearances dataset as dataframe')
            event_app_df.to_parquet(self.ingestion_config.event_appearances_data_path)
            logging.info('Saved the event appearances dataset in parquet format')

            events_df = pd.read_csv('data/events.csv')
            logging.info('Read the events dataset as dataframe')
            events_df.to_parquet(self.ingestion_config.events_data_path)
            logging.info('Saved the events dataset in parquet format')

            funding_rounds_df = pd.read_csv('data/funding_rounds.csv')
            logging.info('Read the funding rounds dataset as dataframe')
            funding_rounds_df.to_parquet(self.ingestion_config.funding_rounds_data_path)
            logging.info('Saved the funding rounds dataset in parquet format')

            funds_df = pd.read_csv('data/funds.csv')
            logging.info('Read the funds dataset as dataframe')
            funds_df.to_parquet(self.ingestion_config.funds_data_path)
            logging.info('Saved the funds dataset in parquet format')

            inv_partn_df = pd.read_csv('data/investment_partners.csv')
            logging.info('Read the investment partners dataset as dataframe')
            inv_partn_df.to_parquet(self.ingestion_config.investments_partners_data_path)
            logging.info('Saved the investment partners dataset in parquet format')

            inv_df = pd.read_csv('data/investments.csv')
            logging.info('Read the investments dataset as dataframe')
            inv_df.to_parquet(self.ingestion_config.investments_data_path)
            logging.info('Saved the investments dataset in parquet format')

            investors_df = pd.read_csv('data/investors.csv')
            logging.info('Read the investors dataset as dataframe')
            investors_df.to_parquet(self.ingestion_config.investors_data_path)
            logging.info('Saved the investors dataset in parquet format')

            ipos_df = pd.read_csv('data/ipos.csv')
            logging.info('Read the ipos dataset as dataframe')
            ipos_df.to_parquet(self.ingestion_config.ipos_data_path)
            logging.info('Saved the ipos dataset in parquet format')

            jobs_df = pd.read_csv('data/jobs.csv')
            logging.info('Read the jobs dataset as dataframe')
            jobs_df.to_parquet(self.ingestion_config.jobs_data_path)
            logging.info('Saved the jobs dataset in parquet format')

            org_parents_df = pd.read_csv('data/org_parents.csv')
            logging.info('Read the organisation parents dataset as dataframe')
            org_parents_df.to_parquet(self.ingestion_config.org_parents_data_path)
            logging.info('Saved the organisation parents dataset in parquet format')

            organization_descriptions_df = pd.read_csv('data/organization_descriptions.csv')
            logging.info('Read the organization_descriptions dataset as dataframe')
            organization_descriptions_df.to_parquet(self.ingestion_config.organization_descriptions_data_path)
            logging.info('Saved the organization_descriptions dataset in parquet format')

            organizations_df = pd.read_csv('data/organizations.csv')
            logging.info('Read the organizations dataset as dataframe')
            organizations_df.to_parquet(self.ingestion_config.organizations_data_path)
            logging.info('Saved the organizations dataset in parquet format')

            people_df = pd.read_csv('data/people.csv')
            logging.info('Read the people dataset as dataframe')
            people_df.to_parquet(self.ingestion_config.people_data_path)
            logging.info('Saved the people dataset in parquet format')

            people_descriptions_df = pd.read_csv('data/people_descriptions.csv')
            logging.info('Read the people_descriptions dataset as dataframe')
            people_descriptions_df.to_parquet(self.ingestion_config.people_descriptions_data_path)
            logging.info('Saved the people_descriptions dataset in parquet format')

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
            raise CustomException(e)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()



