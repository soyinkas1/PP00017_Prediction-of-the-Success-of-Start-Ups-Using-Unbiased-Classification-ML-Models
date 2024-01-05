from dataclasses import dataclass
from pathlib import Path


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

    acquisition_column_to_drop: list
    acquisition_column_to_rename : dict
    cat_groups_column_to_drop: list
    degrees_column_to_drop: list
    event_appearances_column_to_drop: list
    events_column_to_drop: list
    funding_rounds_column_to_drop: list
    funds_column_to_drop: list
    investments_partners_column_to_drop: list
    investments_column_to_drop: list
    investors_column_to_drop: list
    ipos_column_to_drop: list
    jobs_column_to_drop: list
    org_parents_column_to_drop: list
    organization_descriptions_column_to_drop: list
    organizations_column_to_drop: list
    people_column_to_drop: list
    people_descriptions_column_to_drop: list

    acquisition_column_to_drop_na: list
    cat_groups_column_to_drop_na: list
    degrees_column_to_drop_na: list
    event_appearances_column_to_drop_na: list
    events_column_to_drop_na: list
    funding_rounds_column_to_drop_na: list
    funds_column_to_drop_na: list
    investments_partners_column_to_drop_na: list
    investments_column_to_drop_na: list
    investors_column_to_drop_na: list
    ipos_column_to_drop_na: list
    jobs_column_to_drop_na: list
    org_parents_column_to_drop_na: list
    organization_descriptions_column_to_drop_na: list
    organizations_column_to_drop_na: list
    people_column_to_drop_na: list
    people_descriptions_column_to_drop_na: list

    completed_on: str
    started_on: str
    founded_on: str
    closed_on: str
    description: str
