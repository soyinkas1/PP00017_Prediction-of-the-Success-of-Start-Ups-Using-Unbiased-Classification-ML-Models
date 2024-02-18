# Import the required libraries
import pandas as pd
import numpy as np
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException
import warnings
from src.entity.config_entity import DataCleaningConfig, DataIngestionConfig
from datetime import date
import re
import sys
warnings.filterwarnings("ignore")


class DataCleaning:

    def __init__(self, config: DataCleaningConfig, ingest_config: DataIngestionConfig):
        self.cleaning_config = config
        self.ingestion_config = ingest_config

    def clean_data(self):
            
        try:
            # Ingest data
            data_ingestion = DataIngestion(self.ingestion_config)
            data_ingestion.initiate_data_ingestion()

            # Acquisition dataset cleaning

            logging.info('Cleaning acquisition dataset...')
            acquisitions = pd.read_csv(self.ingestion_config.acquisition_local_data_file, low_memory=True)
            # Remove the unneeded columns
            acquisitions.drop(self.cleaning_config.acquisition_column_to_drop, axis=1, inplace=True)
            # Rename columns
            acquisitions.rename(columns=self.cleaning_config.acquisition_column_to_rename, inplace=True)
            # Missing string values (addresses etc.) filled with "not known and numeric values with 0
            for col in acquisitions.columns:
                if acquisitions[col].dtype == 'O':
                    acquisitions[col] = acquisitions[col].astype("string")
                    acquisitions[col].fillna('not known', inplace=True)
                else:
                    acquisitions[col].fillna(0, inplace=True)
            # Save the clean version of the dataset
            acquisitions.to_csv(self.cleaning_config.acquisition_local_data_file, index=False)

            # Degrees dataset cleaning

            logging.info('Cleaning degrees dataset...')
            degrees = pd.read_csv(self.ingestion_config.degrees_local_data_file, low_memory=True)
            # Remove the unneeded columns
            degrees.drop(self.cleaning_config.degrees_column_to_drop, axis=1, inplace=True)
            # Rename started_on and completed_on to make distinct
            degrees.rename(columns=self.cleaning_config.degrees_column_to_rename, inplace=True)
            # Convert the started_on and completed_on to DateTime data type
            degrees[self.cleaning_config.degree_completed_on] = \
                pd.to_datetime(degrees[self.cleaning_config.degree_completed_on], errors='coerce')
            degrees[self.cleaning_config.degree_started_on] = \
                pd.to_datetime(degrees[self.cleaning_config.degree_started_on], errors='coerce')
            # Fill the started_on date with 4 years less than completed_on date
            degrees.loc[degrees[self.cleaning_config.degree_started_on].isna() & degrees[
                self.cleaning_config.degree_completed_on].notna(), self.cleaning_config.degree_started_on] = \
                degrees[self.cleaning_config.degree_completed_on] - pd.offsets.DateOffset(years=4)

            # Fill the completed_on date with 4 years more than started_on date
            degrees.loc[degrees[self.cleaning_config.degree_completed_on].isna() & degrees[
                self.cleaning_config.degree_started_on].notna(), self.cleaning_config.degree_completed_on] = \
                degrees[self.cleaning_config.degree_started_on] + pd.offsets.DateOffset(years=4)
            # Drop the rows with no degree_type, no subject, no started_on, no completed_on.
            degrees.dropna(subset=self.cleaning_config.degrees_column_to_drop_na, inplace=True)
            # Save the clean version of the dataset
            degrees.to_csv(self.cleaning_config.degrees_local_data_file, index=False)

            # Event_appearances dataset cleaning

            logging.info('Cleaning event appearances dataset...')
            event_appearances = pd.read_csv(self.ingestion_config.event_appearances_local_data_file, low_memory=True)
            # Remove the unneeded columns
            event_appearances.drop(self.cleaning_config.event_appearances_column_to_drop, axis=1, inplace=True)
            # Drop rows with missing values
            event_appearances.dropna(inplace=True)
            # Save the clean version of the dataset
            event_appearances.to_csv(self.cleaning_config.event_appearances_local_data_file, index=False)

            # Funding rounds dataset cleaning

            logging.info('Cleaning funding rounds dataset...')
            funding_rounds = pd.read_csv(self.ingestion_config.funding_rounds_local_data_file, low_memory=True)
            # Remove the unneeded columns
            funding_rounds.drop(self.cleaning_config.funding_rounds_column_to_drop, axis=1,
                                inplace=True)
            # Missing string columns will be imputed with "not known" and numerical values will be imputed with 0
            for col in funding_rounds.columns:
                if funding_rounds[col].dtype == 'O':
                    funding_rounds[col] = funding_rounds[col].astype("string")
                    funding_rounds[col].fillna('not known', inplace=True)
                else:
                    funding_rounds[col].fillna(0, inplace=True)
            # Save the clean version of the dataset
            funding_rounds.to_csv(self.cleaning_config.funding_rounds_local_data_file, index=False)

            # Ipos dataset cleaning

            logging.info('Cleaning Ipos dataset...')
            ipos = pd.read_csv(self.ingestion_config.ipos_local_data_file, low_memory=True)

            # Remove the unneeded columns
            ipos.drop(self.cleaning_config.ipos_column_to_drop, axis=1, inplace=True)

            # Rename columns
            ipos.rename(columns=self.cleaning_config.ipos_column_to_rename)

            # Missing string values (addresses etc.) filled with "not known and numeric values with 0
            for col in ipos.columns:
                if ipos[col].dtype == 'O':
                    ipos[col] = ipos[col].astype("string")
                    ipos[col].fillna('not known', inplace=True)
                else:
                    ipos[col].fillna(0, inplace=True)
            # Save the clean version of the dataset
            ipos.to_csv(self.cleaning_config.ipos_local_data_file, index=False)

            # Jobs dataset cleaning

            logging.info('Cleaning jobs dataset...')
            jobs = pd.read_csv(self.ingestion_config.jobs_local_data_file, low_memory=True)
            # Remove the unneeded columns
            jobs.drop(self.cleaning_config.jobs_column_to_drop, axis=1, inplace=True)
            # rename started_on and completed_on to make distinct
            jobs.rename(columns=self.cleaning_config.jobs_column_to_rename, inplace=True)
            # Rows with missing personnel names, uuid and org_name will be dropped
            jobs.dropna(subset=self.cleaning_config.jobs_column_to_drop_na, inplace=True)
            # Convert the started_on and ended_on to DateTime data type
            jobs[self.cleaning_config.job_started_on] = pd.to_datetime(jobs[self.cleaning_config.job_started_on],
                                                                    errors='coerce')
            jobs[self.cleaning_config.job_ended_on] = pd.to_datetime(jobs[self.cleaning_config.job_ended_on],
                                                                    errors='coerce')
            #  fill_na "ended-on" with today's date.
            jobs[self.cleaning_config.job_ended_on].fillna(np.datetime64(date.today()), inplace=True)
            # Save the clean version of the dataset
            jobs.to_csv(self.cleaning_config.jobs_local_data_file, index=False)

            # Organisation parents dataset cleaning

            logging.info('Cleaning org parents dataset...')
            org_parents = pd.read_csv(self.ingestion_config.org_parents_local_data_file, low_memory=True)
            # Remove the unneeded columns
            org_parents.drop(self.cleaning_config.org_parents_column_to_drop, axis=1, inplace=True)
            # rename uuid and name column to make distinct
            org_parents.rename(columns=self.cleaning_config.org_parents_column_to_rename, inplace=True)
            # Save the clean version of the dataset
            org_parents.to_csv(self.cleaning_config.org_parents_local_data_file, index=False)

            # Organisations dataset cleaning

            logging.info('Cleaning organisations dataset...')
            organizations = pd.read_csv(self.ingestion_config.organizations_local_data_file, low_memory=True)
            # Remove the unneeded columns
            organizations.drop(self.cleaning_config.organizations_column_to_drop, axis=1, inplace=True)
            # Convert the started_on , last_funding_on and completed_on to DateTime data type
            organizations[self.cleaning_config.founded_on] = pd.to_datetime(organizations[self.cleaning_config.founded_on],
                                                                            errors='coerce')
            organizations[self.cleaning_config.closed_on] = pd.to_datetime(organizations[self.cleaning_config.closed_on],
                                                                        errors='coerce')
            organizations[self.cleaning_config.last_funding_on] = pd.to_datetime(organizations[
                                                                    self.cleaning_config.last_funding_on], errors='coerce')
            # Fill the rows with no degree_type, no subject, no started_on, no completed_on.
            for col in organizations.columns:
                if organizations[col].dtype == 'O':
                    if not col == 'employee_count':
                        organizations[col] = organizations[col].astype("string")
                        organizations[col].fillna('not known', inplace=True)
                elif not organizations[col].dtype == '<M8[ns]':
                    organizations[col].fillna(0, inplace=True)
            # Drop organisations without twitter_url, facebook_url, founded_on and closed_on values
            organizations.dropna(subset=self.cleaning_config.organizations_column_to_drop_na, inplace=True)
            #  fill_na "closed-on" and last_funding_on" with today's date.
            organizations[self.cleaning_config.closed_on].fillna(np.datetime64(date.today()), inplace=True)
            organizations[self.cleaning_config.last_funding_on].fillna(np.datetime64(date.today()), inplace=True)
            # Extract the lower bound number from the employee_count column
            organizations[self.cleaning_config.employee_count] = organizations[self.cleaning_config.employee_count].\
                apply(lambda x: re.sub("\d+$", " ", x))
            organizations[self.cleaning_config.employee_count] = organizations[self.cleaning_config.employee_count].\
                apply(lambda x: re.sub(r"unknown", "0", x))
            organizations[self.cleaning_config.employee_count] = organizations[self.cleaning_config.employee_count].\
                apply(lambda x: re.sub("[- +]", " ", x))
            # Cast the data type as an int
            organizations[self.cleaning_config.employee_count] = organizations[self.cleaning_config.employee_count].\
                astype(int)
            # Save the clean version of the dataset
            organizations.to_csv(self.cleaning_config.organizations_local_data_file, index=False)

            # Organisation descriptions dataset cleaning

            logging.info('Cleaning organisation descriptions dataset...')
            organization_descriptions = pd.read_csv(self.ingestion_config.organization_descriptions_local_data_file,
                                                    low_memory=True)
            # Remove the unneeded columns
            organization_descriptions.drop(self.cleaning_config.organization_descriptions_column_to_drop, axis=1,
                                        inplace=True)
            # Rename 'description' column to make distinct
            organization_descriptions.rename(columns=self.cleaning_config.organization_descriptions_column_to_rename,
                                            inplace=True)
            # Drop the organisations without names
            organization_descriptions.dropna(subset=self.cleaning_config.organization_descriptions_column_to_drop_na,
                                            axis=0, inplace=True)
            # Organisations without descriptions should be imputed with 'no description'
            organization_descriptions[self.cleaning_config.organization_description].fillna('no description', inplace=True)
            # Save the clean version of the dataset
            organization_descriptions.to_csv(self.cleaning_config.organization_descriptions_local_data_file, index=False)

            # People dataset cleaning
            logging.info('Cleaning people dataset...')
            people = pd.read_csv(self.ingestion_config.people_local_data_file, low_memory=True)
            # Remove the unneeded columns
            people.drop(self.cleaning_config.people_column_to_drop, axis=1, inplace=True)
            # Rename 'facebook_url','linkedin_url', 'twitter_url' columns to make distinct
            people.rename(columns=self.cleaning_config.people_column_to_rename, inplace=True)
            # Drop rows with missing names and organisation_uuid
            people.dropna(subset=self.cleaning_config.people_column_to_drop_na, inplace=True)
            # All other missing values will be imputed with "not known"
            people.fillna('not known', inplace=True)
            # Save the clean version of the dataset
            people.to_csv(self.cleaning_config.people_local_data_file, index=False)

            # People descriptions dataset

            logging.info('Cleaning people description dataset...')
            people_descriptions = pd.read_csv(self.ingestion_config.people_descriptions_local_data_file, low_memory=True)
            # Remove the unneeded columns
            people_descriptions.drop(self.cleaning_config.people_descriptions_column_to_drop, axis=1, inplace=True)
            # Rename the uuid column to people_uuid
            people_descriptions.rename(columns=self.cleaning_config.people_descriptions_column_to_rename, inplace=True)
            # Missing descriptions will be imputed with "no description"
            people_descriptions[self.cleaning_config.people_description].fillna('no description', inplace=True)
            # Save the clean version of the dataset
            people_descriptions.to_csv(self.cleaning_config.people_descriptions_local_data_file, index=False)

            logging.info('First level cleaning of all datasets completed...')

        except Exception as e:
            raise CustomException(e, sys)


    def merge_for_backbone_dataset(self):
        try:
            logging.info('Merging of dataset starting...')
            # import the clean version of datasets that would provide features for the backbone dataset (organizaations)
            organizations = pd.read_csv(self.cleaning_config.organizations_local_data_file,
                                        parse_dates=[self.cleaning_config.founded_on, self.cleaning_config.closed_on])
            # import the clean version of datasets that would provide features for the backbone dataset (organizaation_descriptions)
            organization_descriptions = pd.read_csv(self.cleaning_config.organization_descriptions_local_data_file)
            # Merge with the organization_description table to add the description of the organisation
            logging.info('Merging in organization datasets...')
            backbone_ds = pd.merge(organizations, organization_descriptions, on=self.cleaning_config.uuid, how='inner')
            # import the clean version of datasets that would provide features for the backbone dataset (people)
            people = pd.read_csv(self.cleaning_config.people_local_data_file)
            # Add the people to the backbone dataset
            logging.info('Merging in people datasets...')
            backbone_ds = pd.merge(backbone_ds, people, right_on=self.cleaning_config.featured_job_organization_uuid,
                                left_on=self.cleaning_config.uuid, how='inner')
            # import the clean version of datasets that would provide features for the backbone dataset (people_description)
            people_descriptions = pd.read_csv(self.cleaning_config.people_descriptions_local_data_file)
            # Add the people description to the backbone dataset
            backbone_ds = pd.merge(backbone_ds, people_descriptions, on=self.cleaning_config.person_uuid, how='inner')
            # import the clean version of datasets that would provide features for the backbone dataset (degrees)
            degrees = pd.read_csv(self.cleaning_config.degrees_local_data_file)
            # Add the degrees to the backbone dataset
            logging.info('Merging in degrees datasets...')
            backbone_ds = pd.merge(backbone_ds, degrees, on=self.cleaning_config.person_uuid, how='left')
            # import the clean version of datasets that would provide features for the backbone dataset (events appearances)
            event_appearances = pd.read_csv(self.cleaning_config.event_appearances_local_data_file)
            # Find the number of events participated in
            event_df_ds = pd.DataFrame(event_appearances.groupby(self.cleaning_config.event_group_by)[self.
                                    cleaning_config.event_uuid].count())
            # Reset the index to default
            event_df_ds.reset_index(inplace=True)
            # Create new columns for role in event
            event_df_ds = event_df_ds.pivot(index=self.cleaning_config.participant_uuid,
                                            columns=self.cleaning_config.appearance_type)[self.cleaning_config.event_uuid]
            # Fill the missing values with 0
            event_df_ds.fillna(0, inplace=True)
            # Add the events dataset to the backbone dataset
            logging.info('Merging in events datasets...')
            backbone_ds = pd.merge(backbone_ds, event_df_ds, right_on=self.cleaning_config.participant_uuid,
                                left_on=self.cleaning_config.uuid, how='left')

            # import the clean version of datasets that would provide features for the backbone dataset (acquisitions)
            acquisitions = pd.read_csv(self.cleaning_config.acquisition_local_data_file)
            # import the clean version of datasets that would provide features for the backbone dataset (funding_rounds)
            funding_rounds = pd.read_csv(self.cleaning_config.funding_rounds_local_data_file)
            # import the clean version of datasets that would provide features for the backbone dataset (ipos)
            ipos = pd.read_csv(self.cleaning_config.ipos_local_data_file)
            # Merge the fund raising and acquisition datasets
            success_ds = pd.merge(acquisitions, funding_rounds, on=self.cleaning_config.org_uuid, how='outer')
            # Merge the new fund raising dataset and ipos dataset
            success_ds = pd.merge(success_ds, ipos, on=self.cleaning_config.org_uuid, how='outer')
            # Columns with above values for investment type will be deleted from the funding DataFrame
            failure = ['series_a', 'seed', 'angel', 'debt_financing', 'series_unknown','grant', 'pre_seed']
            for r, col in enumerate(success_ds['investment_type']):
                for fail in failure:
                    if col == fail:
                        success_ds.drop(r, axis=0, inplace=True)
            # Drop all NaN in the investment_type column
            success_ds.dropna(subset=['investment_type'], inplace=True)
            # Create the success column with 1 to represent successful companies on this list
            success_ds['success'] = 1
            # Drop all columns apart from the org_uuid and success columns
            success_ds.drop(self.cleaning_config.success_column_to_drop, axis=1, inplace=True)
            # The success_ds will now be merged with the backbone_ds.
            backbone_ds = pd.merge(backbone_ds, success_ds, right_on=self.cleaning_config.org_uuid,
                                left_on=self.cleaning_config.uuid, how='left')
            # Companies not on this success Dataframe will have value filled with 0 (failure)
            backbone_ds['success'].fillna(0, inplace=True)
            # cast the success column as INT
            backbone_ds['success'] = backbone_ds['success'].astype(int)
            # Save the backbone_ds before merging with the scraped dataset, cleaning and preparing for model training
            backbone_ds.to_csv(self.cleaning_config.unclean_backbone_local_data_file, index=False)

        except Exception as e:
            raise CustomException(e, sys)














