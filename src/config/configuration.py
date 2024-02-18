from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, DataCleaningConfig, DataEnrichConfig, DataScrappingConfig, DataTransformationConfig


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
            n_rows=config.n_rows,
            acquisition_source_data_file=config.acquisition_source_data_file,
            cat_groups_source_data_file=config.cat_groups_source_data_file,
            degrees_source_data_file=config.degrees_source_data_file,
            event_appearances_source_data_file=config.event_appearances_source_data_file,
            events_source_data_file=config.events_source_data_file,
            funding_rounds_source_data_file=config.funding_rounds_source_data_file,
            funds_source_data_file=config.funds_source_data_file,
            investments_partners_source_data_file=config.investments_partners_source_data_file,
            investments_source_data_file=config.investments_source_data_file,
            investors_source_data_file=config.investors_source_data_file,
            ipos_source_data_file=config.ipos_source_data_file,
            jobs_source_data_file=config.jobs_source_data_file,
            org_parents_source_data_file=config.org_parents_source_data_file,
            organization_descriptions_source_data_file=config.organization_descriptions_source_data_file,
            organizations_source_data_file=config.organizations_source_data_file,
            people_source_data_file=config.people_source_data_file,
            people_descriptions_source_data_file=config.people_descriptions_source_data_file,
            acquisition_local_data_file=config.acquisition_local_data_file,
            cat_groups_local_data_file=config.cat_groups_local_data_file,
            degrees_local_data_file=config.degrees_local_data_file,
            event_appearances_local_data_file=config.event_appearances_local_data_file,
            events_local_data_file=config.events_local_data_file,
            funding_rounds_local_data_file=config.funding_rounds_local_data_file,
            funds_local_data_file=config.funds_local_data_file,
            investments_partners_local_data_file=config.investments_partners_local_data_file,
            investments_local_data_file=config.investments_local_data_file,
            investors_local_data_file=config.investors_local_data_file,
            ipos_local_data_file=config.ipos_local_data_file,
            jobs_local_data_file=config.jobs_local_data_file,
            org_parents_local_data_file=config.org_parents_local_data_file,
            organization_descriptions_local_data_file=config.organization_descriptions_local_data_file,
            organizations_local_data_file=config.organizations_local_data_file,
            people_local_data_file=config.people_local_data_file,
            people_descriptions_local_data_file=config.people_descriptions_local_data_file

        )

        return data_ingestion_config

    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config.data_cleaning

        create_directories([config.root_dir])

        data_cleaning_config = DataCleaningConfig(
            root_dir=config.root_dir,
            acquisition_local_data_file=config.acquisition_local_data_file,
            degrees_local_data_file=config.degrees_local_data_file,
            event_appearances_local_data_file=config.event_appearances_local_data_file,
            funding_rounds_local_data_file=config.funding_rounds_local_data_file,
            ipos_local_data_file=config.ipos_local_data_file,
            jobs_local_data_file=config.jobs_local_data_file,
            org_parents_local_data_file=config.org_parents_local_data_file,
            organization_descriptions_local_data_file=config.organization_descriptions_local_data_file,
            organizations_local_data_file=config.organizations_local_data_file,
            people_local_data_file=config.people_local_data_file,
            people_descriptions_local_data_file=config.people_descriptions_local_data_file,
            acquisition_column_to_drop=config.acquisition_column_to_drop,
            acquisition_column_to_rename=config.acquisition_column_to_rename,
            degrees_column_to_drop=config.degrees_column_to_drop,
            degrees_column_to_rename=config.degrees_column_to_rename,
            degrees_column_to_drop_na=config.degrees_column_to_drop_na,
            event_appearances_column_to_drop=config.event_appearances_column_to_drop,
            funding_rounds_column_to_drop=config.funding_rounds_column_to_drop,
            ipos_column_to_drop=config.ipos_column_to_drop,
            jobs_column_to_drop=config.jobs_column_to_drop,
            jobs_column_to_rename=config.jobs_column_to_rename,
            jobs_column_to_drop_na=config.jobs_column_to_drop_na,
            org_parents_column_to_drop=config.org_parents_column_to_drop,
            org_parents_column_to_rename=config.org_parents_column_to_rename,
            organizations_column_to_drop=config.organizations_column_to_drop,
            organizations_column_to_drop_na=config.organizations_column_to_drop_na,
            organization_descriptions_column_to_drop=config.organization_descriptions_column_to_drop,
            organization_descriptions_column_to_rename=config.organization_descriptions_column_to_rename,
            organization_descriptions_column_to_drop_na=config.organization_descriptions_column_to_drop_na,
            people_column_to_drop=config.people_column_to_drop,
            people_column_to_rename=config.people_column_to_rename,
            people_column_to_drop_na=config.people_column_to_drop_na,
            people_descriptions_column_to_drop=config.people_descriptions_column_to_drop,
            people_descriptions_column_to_rename=config.people_descriptions_column_to_rename,
            degree_completed_on=config.degree_completed_on,
            degree_started_on=config.degree_started_on,
            founded_on=config.founded_on,
            closed_on=config.closed_on,
            last_funding_on=config.last_funding_on,
            description=config.description,
            job_started_on=config.job_started_on,
            job_ended_on=config.job_ended_on,
            employee_count=config.employee_count,
            organization_description=config.organization_description,
            people_description=config.people_description,
            uuid=config.uuid,
            featured_job_organization_uuid=config.featured_job_organization_uuid,
            person_uuid=config.person_uuid,
            event_uuid=config.event_uuid,
            participant_uuid=config.participant_uuid,
            appearance_type=config.appearance_type,
            event_group_by=config.event_group_by,
            org_uuid=config.org_uuid,
            unclean_backbone_local_data_file=config.unclean_backbone_local_data_file,
            success_column_to_drop=config.success_column_to_drop

        )

        return data_cleaning_config

    def get_data_scrapping_config(self) -> DataScrappingConfig:
        config = self.config.data_scrapping

        create_directories([config.root_dir])

        data_scrapping_config = DataScrappingConfig(
            root_dir=config.root_dir,
            chrome_driver_path=config.chrome_driver_path,
            unclean_backbone_local_data_file=config.unclean_backbone_local_data_file,
            twitter_url=config.twitter_url,
            facebook_url=config.facebook_url,
            twitter_username=config.twitter_username,
            twitter_password=config.twitter_password,
            df_rows=config.df_rows,
            max_tweets=config.max_tweets,
            facebook_username=config.facebook_username,
            facebook_password=config.facebook_password,

        )

        return data_scrapping_config

    def get_data_enrich_config(self) -> DataEnrichConfig:
        config = self.config.data_enrich

        create_directories([config.root_dir])

        data_enrich_config = DataEnrichConfig(
            root_dir=config.root_dir,
            twitter_sentiment_local_data_file=config.twitter_sentiment_local_data_file,
            enriched_backbone_local_data_file=config.enriched_backbone_local_data_file,
            column_to_load=config.column_to_load,
            follower_data=config.follower_data,
            following_data=config.following_data,
            account=config.account,
            polarity=config.polarity,
            subjectivity=config.subjectivity,
            tweet_analysis=config.tweet_analysis,
            text=config.text,
            enrich_data_columns=config.enrich_data_columns




        )

        return data_enrich_config
    
    def get_data_transfrom_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transform_config = DataTransformationConfig(
                root_dir = config.root_dir,
                clean_backbone_local_data_file=config.
                transformed_data_local_data_file: Path
                train_data_local_data_file: Path
                validate_data_local_data_file: Path
                test_data_local_data_file: Path
                per_exp_at_coy_start: str 
                founded_on: str
                closed_on: str
                degree_completed_on: str
                degree_length: str
                yrs_since_last_funding: str
                yrs_of_operation: str
                columns_to_parse_dates: list
                columns_to_drop: list
                columns_rearrangement: list
                institution_name: str
                degree_type: str
                subject: str
                degree_is_completed: str
                exhibitor: str
                organizer: str
                speaker:str 
                sponsor:str
                last_funding_on: str
                employee_cap_success: int
                employee_count: str
                success: str
                uuid: str
                train_percent: float
                validate_percent: float
                test_percent: float




        )

        return data_enrich_config


