from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    n_rows: int
    acquisition_source_data_file: Path
    cat_groups_source_data_file: Path
    degrees_source_data_file: Path
    event_appearances_source_data_file: Path
    events_source_data_file: Path
    funding_rounds_source_data_file: Path
    funds_source_data_file: Path
    investments_partners_source_data_file: Path
    investments_source_data_file: Path
    investors_source_data_file: Path
    ipos_source_data_file: Path
    jobs_source_data_file: Path
    org_parents_source_data_file: Path
    organization_descriptions_source_data_file: Path
    organizations_source_data_file: Path
    people_source_data_file: Path
    people_descriptions_source_data_file: Path

    acquisition_local_data_file: Path
    cat_groups_local_data_file: Path
    degrees_local_data_file: Path
    event_appearances_local_data_file: Path
    events_local_data_file: Path
    funding_rounds_local_data_file: Path
    funds_local_data_file: Path
    investments_partners_local_data_file: Path
    investments_local_data_file: Path
    investors_local_data_file: Path
    ipos_local_data_file: Path
    jobs_local_data_file: Path
    org_parents_local_data_file: Path
    organization_descriptions_local_data_file: Path
    organizations_local_data_file: Path
    people_local_data_file: Path
    people_descriptions_local_data_file: Path


@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir: Path
    acquisition_local_data_file: Path
    degrees_local_data_file: Path
    event_appearances_local_data_file: Path
    funding_rounds_local_data_file: Path
    ipos_local_data_file: Path
    jobs_local_data_file: Path
    org_parents_local_data_file: Path
    organization_descriptions_local_data_file: Path
    organizations_local_data_file: Path
    people_local_data_file: Path
    people_descriptions_local_data_file: Path

    acquisition_column_to_drop: list
    acquisition_column_to_rename: dict
    degrees_column_to_drop: list
    degrees_column_to_rename: dict
    degrees_column_to_drop_na: list
    event_appearances_column_to_drop: list
    funding_rounds_column_to_drop: list
    ipos_column_to_drop: list
    ipos_column_to_rename: dict
    jobs_column_to_drop: list
    jobs_column_to_rename: dict
    jobs_column_to_drop_na: list
    org_parents_column_to_drop: list
    org_parents_column_to_rename: dict
    organizations_column_to_drop: list
    organizations_column_to_drop_na: list
    organization_descriptions_column_to_drop: list
    organization_descriptions_column_to_rename: dict
    organization_descriptions_column_to_drop_na: list
    people_column_to_drop: list
    people_column_to_rename: dict
    people_column_to_drop_na: list
    people_descriptions_column_to_drop: list
    people_descriptions_column_to_rename: dict

    degree_completed_on: str
    degree_started_on: str
    founded_on: str
    closed_on: str
    last_funding_on: str
    description: str
    job_started_on: str
    job_ended_on: str
    employee_count: str
    organization_description: str
    people_description: str

    uuid: str
    featured_job_organization_uuid: str
    person_uuid: str
    event_uuid: str
    participant_uuid: str
    appearance_type: str
    event_group_by: list
    org_uuid: str
    clean_backbone_local_data_file: Path
    success_column_to_drop: list


@dataclass(frozen=True)
class DataEnrichConfig:
    root_dir: Path
    twitter_sentiment_local_data_file: Path
    enriched_backbone_local_data_file: Path
    column_to_load: list
    follower_data: str
    following_data: str
    account: str
    polarity: str
    subjectivity: str
    tweet_analysis: str
    text: str
    enrich_data_columns: list



@dataclass(frozen=True)
class DataScrappingConfig:
    root_dir: Path
    chrome_driver_path: str
    unclean_backbone_local_data_file: Path
    twitter_url: str
    facebook_url: str
    twitter_username: str
    twitter_password: str
    df_rows: int
    max_tweets: int
    facebook_username: str
    facebook_password: str



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    clean_backbone_local_data_file: Path
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
    num_features: list
    text_feature_o: str
    text_feature_p: str
    cat_features: list
    preprocessor_obj_path: str | os.PathLike


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    validation_data_path: Path
    test_data_path: Path
    best_model_path: Path
    models: dict
    params: dict


@dataclass(frozen=True)
class PredictionPipelineConfig:

    per_exp_at_coy_start: str 
    degree_length: str
    yrs_since_last_funding: str
    yrs_of_operation: str
    institution_name: str
    degree_type: str
    subject: str
    degree_is_completed: str
    exhibitor: str
    organizer: str
    speaker:str 
    sponsor:str
    last_funding_amount: str
    employee_count: str
    model_path: Path
    preprocessor_obj_path: Path
   