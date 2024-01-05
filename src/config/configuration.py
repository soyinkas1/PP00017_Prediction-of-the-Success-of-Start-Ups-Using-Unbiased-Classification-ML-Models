from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, DataCleaningConfig


class ConfigurationManager:

    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        # self.params = read_yaml(params_filepath)
        # self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
        root_dir=config.root_dir,
        n_rows= config.n_rows,
        acquisition_source_data_file = config.acquisition_source_data_file,
        cat_groups_source_data_file = config.cat_groups_source_data_file,
        degrees_source_data_file = config.degrees_source_data_file,
        event_appearances_source_data_file = config.event_appearances_source_data_file,
        events_source_data_file = config.events_source_data_file,
        funding_rounds_source_data_file = config.funding_rounds_source_data_file,
        funds_source_data_file = config.funds_source_data_file,
        investments_partners_source_data_file = config.investments_partners_source_data_file,
        investments_source_data_file = config.investments_source_data_file,
        investors_source_data_file = config.investors_source_data_file,
        ipos_source_data_file = config.ipos_source_data_file,
        jobs_source_data_file = config.jobs_source_data_file,
        org_parents_source_data_file = config.org_parents_source_data_file,
        organization_descriptions_source_data_file = config.organization_descriptions_source_data_file,
        organizations_source_data_file = config.organizations_source_data_file,
        people_source_data_file = config. people_source_data_file,
        people_descriptions_source_data_file = config.people_descriptions_source_data_file,
        acquisition_local_data_file = config.acquisition_local_data_file,
        cat_groups_local_data_file = config.cat_groups_local_data_file,
        degrees_local_data_file = config.degrees_local_data_file,
        event_appearances_local_data_file = config.event_appearances_local_data_file,
        events_local_data_file = config.events_local_data_file,
        funding_rounds_local_data_file = config.funding_rounds_local_data_file,
        funds_local_data_file = config.funds_local_data_file,
        investments_partners_local_data_file = config.investments_partners_local_data_file,
        investments_local_data_file = config.investments_local_data_file,
        investors_local_data_file = config.investors_local_data_file,
        ipos_local_data_file = config.ipos_local_data_file,
        jobs_local_data_file = config.jobs_local_data_file,
        org_parents_local_data_file = config.org_parents_local_data_file,
        organization_descriptions_local_data_file = config.organization_descriptions_local_data_file,
        organizations_local_data_file = config.organizations_local_data_file,
        people_local_data_file = config.people_local_data_file,
        people_descriptions_local_data_file = config.people_descriptions_local_data_file

        )

        return data_ingestion_config

    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config.data_cleaning

        create_directories([config.root_dir])

        data_cleaning_config = DataCleaningConfig(
        root_dir = config.root_dir,
        acquisition_local_data_file = config.acquisition_local_data_file,
        cat_groups_local_data_file = config.cat_groups_local_data_file,
        degrees_local_data_file = config.degrees_local_data_file,
        event_appearances_local_data_file = config.event_appearances_local_data_file,
        events_local_data_file = config.events_local_data_file,
        funding_rounds_local_data_file = config.funding_rounds_local_data_file,
        funds_local_data_file = config.funds_local_data_file,
        investments_partners_local_data_file = config.investments_partners_local_data_file,
        investments_local_data_file = config.investments_local_data_file,
        investors_local_data_file = config.investors_local_data_file,
        ipos_local_data_file = config.ipos_local_data_file,
        jobs_local_data_file = config.jobs_local_data_file,
        org_parents_local_data_file = config.org_parents_local_data_file,
        organization_descriptions_local_data_file = config.organization_descriptions_local_data_file,
        organizations_local_data_file = config.organizations_local_data_file,
        people_local_data_file = config.people_local_data_file,
        people_descriptions_local_data_file = config.people_descriptions_local_data_file
        )

        return data_cleaning_config



