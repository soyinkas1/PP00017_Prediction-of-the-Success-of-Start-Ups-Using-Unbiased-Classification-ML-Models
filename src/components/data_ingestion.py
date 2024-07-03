import sys
import pandas as pd
from azure.storage.blob import BlobServiceClient
from src.exception import CustomException
from src.logger import logging
from src.utils.common import download_blob_to_df, upload_dataframe_to_blob
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
            acq_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.acquisition_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the acquisitions dataset as dataframe')
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         acq_df,
                                         self.ingestion_config.acquisition_local_blob_file
                )
            logging.info('Saved the acquisitions dataset to Azure in csv format')

            # deg_dfs = pd.read_csv(self.ingestion_config.degrees_source_data_file, chunksize=chunk_size,
            #                       low_memory=True, nrows=self.ingestion_config.n_rows)
            # deg_df = pd.concat(deg_dfs)

            deg_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.degrees_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the degrees dataset as dataframe')
            # deg_df.to_csv(self.ingestion_config.degrees_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         deg_df,
                                         self.ingestion_config.degrees_local_blob_file)
            
            logging.info('Saved the degrees dataset in csv format')

            # event_app_dfs = pd.read_csv(self.ingestion_config.event_appearances_source_data_file, chunksize=chunk_size,
            #                             low_memory=True, nrows=self.ingestion_config.n_rows)
            # event_app_df = pd.concat(event_app_dfs)
            
            event_app_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.event_appearances_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the event appearances dataset as dataframe')
            # event_app_df.to_csv(self.ingestion_config.event_appearances_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         event_app_df,
                                         self.ingestion_config.event_appearances_local_blob_file)

            logging.info('Saved the event appearances dataset in csv format')


            # funding_rounds_dfs = pd.read_csv(self.ingestion_config.funding_rounds_source_data_file, chunksize=chunk_size,
            #                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            # funding_rounds_df = pd.concat(funding_rounds_dfs)
            
            funding_rounds_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.funding_rounds_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the funding rounds dataset as dataframe')
            # funding_rounds_df.to_csv(self.ingestion_config.funding_rounds_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         funding_rounds_df,
                                         self.ingestion_config.funding_rounds_local_blob_file)
            
            logging.info('Saved the funding rounds dataset in csv format')

            # ipos_dfs = pd.read_csv(self.ingestion_config.ipos_source_data_file, chunksize=chunk_size,
            #                        low_memory=True, nrows=self.ingestion_config.n_rows)
            # ipos_df = pd.concat(ipos_dfs)
            
            ipos_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.ipos_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the ipos dataset as dataframe')
            # ipos_df.to_csv(self.ingestion_config.ipos_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         ipos_df,
                                         self.ingestion_config.ipos_local_blob_file)
            
            logging.info('Saved the ipos dataset in csv format')

            # jobs_dfs = pd.read_csv(self.ingestion_config.jobs_source_data_file, chunksize=chunk_size,
            #                        low_memory=True, nrows=self.ingestion_config.n_rows)
            # jobs_df = pd.concat(jobs_dfs)
            
            jobs_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.jobs_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the jobs dataset as dataframe')
            # jobs_df.to_csv(self.ingestion_config.jobs_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         jobs_df,
                                         self.ingestion_config.jobs_local_blob_file)
            
            logging.info('Saved the jobs dataset in csv format')

            # org_parents_dfs = pd.read_csv(self.ingestion_config.org_parents_source_data_file, chunksize=chunk_size,
            #                               low_memory=True, nrows=self.ingestion_config.n_rows)
            # org_parents_df = pd.concat(org_parents_dfs)
            
            org_parents_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.org_parents_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            
            
            logging.info('Read the organisation parents dataset as dataframe')
            # org_parents_df.to_csv(self.ingestion_config.org_parents_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         org_parents_df,
                                         self.ingestion_config.org_parents_local_blob_file)
            
            logging.info('Saved the organisation parents dataset in csv format')

            # organization_descriptions_dfs = pd.read_csv(self.ingestion_config.organization_descriptions_source_data_file, chunksize=chunk_size,
            #                                             low_memory=True, nrows=self.ingestion_config.n_rows)
            # organization_descriptions_df = pd.concat(organization_descriptions_dfs)
            
            organization_descriptions_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.organization_descriptions_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            
            logging.info('Read the organization_descriptions dataset as dataframe')
            # organization_descriptions_df.to_csv(self.ingestion_config.organization_descriptions_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         organization_descriptions_df,
                                         self.ingestion_config.organization_descriptions_local_blob_file)
            
            logging.info('Saved the organization_descriptions dataset in csv format')

            # organizations_dfs = pd.read_csv(self.ingestion_config.organizations_source_data_file, chunksize=chunk_size,
            #                                 low_memory=True, nrows=self.ingestion_config.n_rows)
            # organizations_df = pd.concat(organizations_dfs)
            
            organizations_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.organizations_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            logging.info('Read the organizations dataset as dataframe')
            # organizations_df.to_csv(self.ingestion_config.organizations_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         organizations_df,
                                         self.ingestion_config.organizations_local_blob_file)
            
            
            
            
            logging.info('Saved the organizations dataset in csv format')

            # people_dfs = pd.read_csv(self.ingestion_config.people_source_data_file, chunksize=chunk_size,
            #                          low_memory=True, nrows=self.ingestion_config.n_rows)
            # people_df = pd.concat(people_dfs)
            
            people_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.people_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            
            
            logging.info('Read the people dataset as dataframe')
            # people_df.to_csv(self.ingestion_config.people_local_data_file, index=False)
            
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         people_df,
                                         self.ingestion_config.people_local_blob_file)
            
            
            
            logging.info('Saved the people dataset in csv format')

            # people_descriptions_dfs = pd.read_csv(self.ingestion_config.people_descriptions_source_data_file,
            #                             chunksize=chunk_size, low_memory=True, nrows=self.ingestion_config.n_rows)
            # people_descriptions_df = pd.concat(people_descriptions_dfs)
            
            
            people_descriptions_df = download_blob_to_df(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                          self.ingestion_config.people_descriptions_source_blob_file, 
                                          chunksize=self.ingestion_config.chunk_size,
                                  low_memory=True, nrows=self.ingestion_config.n_rows)
            
            
            
            logging.info('Read the people_descriptions dataset as dataframe')
            # people_descriptions_df.to_csv(self.ingestion_config.people_descriptions_local_data_file, index=False)
            
            upload_dataframe_to_blob(self.ingestion_config.azure_storage_account_name, 
                                         self.ingestion_config.azure_storage_account_key,
                                         self.ingestion_config.azure_container_name,
                                         people_descriptions_df,
                                         self.ingestion_config.people_descriptions_local_blob_file)
            
            
            
            logging.info('Saved the people_descriptions dataset in csv format')

            logging.info('Ingestion of the data is completed')

 #            
                    

        except Exception as e:
            raise CustomException(e, sys)

# if __name__ == '__main__':
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()



