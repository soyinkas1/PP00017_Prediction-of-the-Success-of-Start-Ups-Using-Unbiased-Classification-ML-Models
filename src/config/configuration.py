from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, DataCleaningConfig, DataEnrichConfig, DataScrappingConfig, DataTransformationConfig, ModelTrainerConfig, PredictionPipelineConfig
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class ConfigurationManager:
   

    SECRET_KEY=os.environ.get('SECRET_KEY')

    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
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
            ipos_column_to_rename=config.ipos_column_to_rename,
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
            clean_backbone_local_data_file=config.clean_backbone_local_data_file,
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
    
    def get_data_transform_config(self, ) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transform_config = DataTransformationConfig(
                root_dir= config.root_dir,
                clean_backbone_local_data_file=config.clean_backbone_local_data_file,
                transformed_data_local_data_file=config.transformed_data_local_data_file,
                train_data_local_data_file=config.train_data_local_data_file,
                validate_data_local_data_file=config.validate_data_local_data_file,
                test_data_local_data_file=config.test_data_local_data_file,
                per_exp_at_coy_start=config.per_exp_at_coy_start,
                founded_on=config.founded_on,
                closed_on=config.closed_on,
                degree_completed_on=config.degree_completed_on,
                degree_length=config.degree_length,
                yrs_since_last_funding=config.yrs_since_last_funding,
                yrs_of_operation=config.yrs_of_operation,
                columns_to_parse_dates=config.columns_to_parse_dates,
                columns_to_drop=config.columns_to_drop,
                columns_rearrangement=config.columns_rearrangement,
                institution_name=config.institution_name,
                degree_type=config.degree_type,
                subject=config.subject,
                degree_is_completed=config.degree_is_completed,
                exhibitor=config.exhibitor,
                organizer=config.organizer,
                speaker=config.speaker,
                sponsor=config.sponsor,
                last_funding_on=config.last_funding_on,
                employee_cap_success=config.employee_cap_success,
                employee_count=config.employee_count,
                success=config.success,
                uuid=config.uuid,
                train_percent=config.train_percent,
                validate_percent=config.validate_percent,
                test_percent=config.test_percent,
                num_features=config.num_features,
                text_feature_o=config.text_feature_o,
                text_feature_p=config.text_feature_p,
                cat_features=config.cat_features,
                preprocessor_obj_path=config.preprocessor_obj_path
                


        )

        return data_transform_config
    
    def get_model_trainer_config(self, ) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.param_grid

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                validation_data_path=config.validation_data_path,
                test_data_path=config.test_data_path,
                best_model_path=config.best_model_path,
                models=config.models,
                params=params.params
                
                
        )

        return model_trainer_config
    
    def get_prediction_pipeline_config(self, ) -> PredictionPipelineConfig:
        config = self.config.prediction_pipeline

        predition_pipeline_config = PredictionPipelineConfig(
                degree_length=config.degree_length,
                yrs_since_last_funding=config.yrs_since_last_funding,
                yrs_of_operation=config.yrs_of_operation,
                institution_name=config.institution_name,
                degree_type=config.degree_type,
                subject=config.subject,
                degree_is_completed=config.degree_is_completed,
                exhibitor=config.exhibitor,
                organizer=config.organizer,
                speaker=config.speaker,
                sponsor=config.sponsor,
                last_funding_amount=config.last_funding_amount,
                employee_count=config.employee_count,
                model_path=config.model_path
                preprocessor_obj_path=config.preprocessor_obj_path
                
                
        )

        return predition_pipeline_config
    




