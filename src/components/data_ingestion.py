import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

import warnings
from src.entity.config_entity import DataIngestionConfig

warnings.filterwarnings("ignore")

class DataIngestion:
    """
    Class object that defines the data ingestion stage of the project
    """
    def __init__(self, config: DataIngestionConfig):
        self.ingestion_config = config

    def initiate_data_ingestion(self):
        """ The method to ingest data from data sources"""
        logging.info('Entered data ingestion method or component')
        chunk_size = 100000
        try:
            # # Create the artifact folder/directory
            # os.makedirs(os.path.dirname(self.ingestion_config.people_data_path), exist_ok=True)
            acq_dfs = pd.read_csv(self.ingestion_config.acquisition_source_data_file, chunksize=chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            acq_df = pd.concat(acq_dfs)
            logging.info('Read the acquisitions dataset as dataframe')
            acq_df.to_csv(self.ingestion_config.acquisition_local_data_file, index=False)
            logging.info('Saved the acquisitions dataset in csv format')

            # catg_dfs = pd.read_csv(self.ingestion_config.cat_groups_source_data_file, chunksize=chunk_size,
            #                        low_memory=True, nrows=self.ingestion_config.n_rows)
            # catg_df = pd.concat(catg_dfs)
            # logging.info('Read the category groups dataset as dataframe')
            # catg_df.to_csv(self.ingestion_config.cat_groups_local_data_file, index=False)
            # logging.info('Saved the category groups dataset in csv format')

            deg_dfs = pd.read_csv(self.ingestion_config.degrees_source_data_file, chunksize=chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            deg_df = pd.concat(deg_dfs)
            logging.info('Read the degrees dataset as dataframe')
            deg_df.to_csv(self.ingestion_config.degrees_local_data_file, index=False)
            logging.info('Saved the degrees dataset in csv format')

            event_app_dfs = pd.read_csv(self.ingestion_config.event_appearances_source_data_file, chunksize=chunk_size,
                                        low_memory=True, nrows=self.ingestion_config.n_rows)
            event_app_df = pd.concat(event_app_dfs)
            logging.info('Read the event appearances dataset as dataframe')
            event_app_df.to_csv(self.ingestion_config.event_appearances_local_data_file, index=False)
            logging.info('Saved the event appearances dataset in csv format')

            # events_dfs = pd.read_csv(self.ingestion_config.events_source_data_file, chunksize=chunk_size,
            #                          low_memory=True, nrows=self.ingestion_config.n_rows)
            # events_df = pd.concat(events_dfs)
            # logging.info('Read the events dataset as dataframe')
            # events_df.to_csv(self.ingestion_config.events_local_data_file, index=False)
            # logging.info('Saved the events dataset in csv format')

            funding_rounds_dfs = pd.read_csv(self.ingestion_config.funding_rounds_source_data_file, chunksize=chunk_size,
                                             low_memory=True, nrows=self.ingestion_config.n_rows)
            funding_rounds_df = pd.concat(funding_rounds_dfs)
            logging.info('Read the funding rounds dataset as dataframe')
            funding_rounds_df.to_csv(self.ingestion_config.funding_rounds_local_data_file, index=False)
            logging.info('Saved the funding rounds dataset in csv format')

            # funds_dfs = pd.read_csv(self.ingestion_config.funds_source_data_file, chunksize=chunk_size,
            #                         low_memory=True, nrows=self.ingestion_config.n_rows)
            # funds_df = pd.concat(funds_dfs)
            # logging.info('Read the funds dataset as dataframe')
            # funds_df.to_csv(self.ingestion_config.funds_local_data_file, index=False)
            # logging.info('Saved the funds dataset in csv format')
            #
            # inv_partn_dfs = pd.read_csv(self.ingestion_config.investments_partners_source_data_file, chunksize=chunk_size,
            #                             low_memory=True, nrows=self.ingestion_config.n_rows)
            # inv_partn_df = pd.concat(inv_partn_dfs)
            # logging.info('Read the investment partners dataset as dataframe')
            # inv_partn_df.to_csv(self.ingestion_config.investments_partners_local_data_file, index=False)
            # logging.info('Saved the investment partners dataset in csv format')
            #
            # inv_dfs = pd.read_csv(self.ingestion_config.investments_source_data_file, chunksize=chunk_size,
            #                       low_memory=True, nrows=self.ingestion_config.n_rows)
            # inv_df = pd.concat(inv_dfs)
            # logging.info('Read the investments dataset as dataframe')
            # inv_df.to_csv(self.ingestion_config.investments_local_data_file, index=False)
            # logging.info('Saved the investments dataset in csv format')
            #
            # investors_dfs = pd.read_csv(self.ingestion_config.investors_source_data_file, chunksize=chunk_size,
            #                             low_memory=True, nrows=self.ingestion_config.n_rows)
            # investors_df = pd.concat(investors_dfs)
            # logging.info('Read the investors dataset as dataframe')
            # investors_df.to_csv(self.ingestion_config.investors_local_data_file, index=False)
            # logging.info('Saved the investors dataset in csv format')

            ipos_dfs = pd.read_csv(self.ingestion_config.ipos_source_data_file, chunksize=chunk_size,
                                   low_memory=True, nrows=self.ingestion_config.n_rows)
            ipos_df = pd.concat(ipos_dfs)
            logging.info('Read the ipos dataset as dataframe')
            ipos_df.to_csv(self.ingestion_config.ipos_local_data_file, index=False)
            logging.info('Saved the ipos dataset in csv format')

            jobs_dfs = pd.read_csv(self.ingestion_config.jobs_source_data_file, chunksize=chunk_size,
                                   low_memory=True, nrows=self.ingestion_config.n_rows)
            jobs_df = pd.concat(jobs_dfs)
            logging.info('Read the jobs dataset as dataframe')
            jobs_df.to_csv(self.ingestion_config.jobs_local_data_file, index=False)
            logging.info('Saved the jobs dataset in csv format')

            org_parents_dfs = pd.read_csv(self.ingestion_config.org_parents_source_data_file, chunksize=chunk_size,
                                          low_memory=True, nrows=self.ingestion_config.n_rows)
            org_parents_df = pd.concat(org_parents_dfs)
            logging.info('Read the organisation parents dataset as dataframe')
            org_parents_df.to_csv(self.ingestion_config.org_parents_local_data_file, index=False)
            logging.info('Saved the organisation parents dataset in csv format')

            organization_descriptions_dfs = pd.read_csv(self.ingestion_config.organization_descriptions_source_data_file, chunksize=chunk_size,
                                                        low_memory=True, nrows=self.ingestion_config.n_rows)
            organization_descriptions_df = pd.concat(organization_descriptions_dfs)
            logging.info('Read the organization_descriptions dataset as dataframe')
            organization_descriptions_df.to_csv(self.ingestion_config.organization_descriptions_local_data_file, index=False)
            logging.info('Saved the organization_descriptions dataset in csv format')

            organizations_dfs = pd.read_csv(self.ingestion_config.organizations_source_data_file, chunksize=chunk_size,
                                            low_memory=True, nrows=self.ingestion_config.n_rows)
            organizations_df = pd.concat(organizations_dfs)
            logging.info('Read the organizations dataset as dataframe')
            organizations_df.to_csv(self.ingestion_config.organizations_local_data_file, index=False)
            logging.info('Saved the organizations dataset in csv format')

            people_dfs = pd.read_csv(self.ingestion_config.people_source_data_file, chunksize=chunk_size,
                                     low_memory=True, nrows=self.ingestion_config.n_rows)
            people_df = pd.concat(people_dfs)
            logging.info('Read the people dataset as dataframe')
            people_df.to_csv(self.ingestion_config.people_local_data_file, index=False)
            logging.info('Saved the people dataset in csv format')

            people_descriptions_dfs = pd.read_csv(self.ingestion_config.people_descriptions_source_data_file,
                                        chunksize=chunk_size, low_memory=True, nrows=self.ingestion_config.n_rows)
            people_descriptions_df = pd.concat(people_descriptions_dfs)
            logging.info('Read the people_descriptions dataset as dataframe')
            people_descriptions_df.to_csv(self.ingestion_config.people_descriptions_local_data_file, index=False)
            logging.info('Saved the people_descriptions dataset in csv format')

            logging.info('Ingestion of the data is completed')

        

        except Exception as e:
            raise CustomException(e, sys)

# if __name__ == '__main__':
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()



