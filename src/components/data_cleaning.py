# Import the required libraries
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.utils import imput_rank
from src.logger import logging
import warnings

warnings.filterwarnings("ignore")


def clean_data():
    # Ingest data
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()

    # Acquisition dataset cleaning

    logging.info('Cleaning acquisition dataset...')
    acquisitions = pd.read_csv('artifacts/acquisitions.csv', low_memory=True)
    # Remove the unneeded columns
    acquisitions.drop(['permalink', 'cb_url', 'rank', 'created_at', 'updated_at',
                       'acquiree_cb_url', 'acquirer_cb_url'], axis=1, inplace=True)
    # Missing price currency code to be filled with USD
    acquisitions['price_currency_code'].fillna('USD', inplace=True)
    # Missing string values (addresses etc.) filled with "not known and numeric values with 0
    for col in acquisitions.columns:
        if acquisitions[col].dtype == 'O':
            acquisitions[col] = acquisitions[col].astype("string")
            acquisitions[col].fillna('not known', inplace=True)
        else:
            acquisitions[col].fillna(0, inplace=True)
    # Save the clean version of the dataset
    acquisitions.to_csv('artifacts/acquisitions.csv', index=False)

    # Category groups dataset cleaning

    logging.info('Cleaning category groups dataset...')
    category_groups = pd.read_csv('artifacts/category_groups.csv', low_memory=True)
    # Remove the unneeded columns
    category_groups.drop(['rank', 'permalink', 'cb_url', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Save the clean version of the dataset
    category_groups.to_csv('artifacts/category_groups.csv', index=False)

    # Degrees dataset cleaning

    logging.info('Cleaning degrees dataset...')
    degrees = pd.read_csv('artifacts/degrees.csv', low_memory=True)
    # Remove the unneeded columns
    degrees.drop(['name', 'rank', 'permalink', 'cb_url', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Convert the started_on and completed_on to DateTime data type
    degrees['completed_on'] = pd.to_datetime(degrees['completed_on'], errors='coerce')
    degrees['started_on'] = pd.to_datetime(degrees['started_on'], errors='coerce')
    # Fill the started_on date with 4 years less than completed_on date
    degrees.loc[degrees['started_on'].isna() & degrees['completed_on'].notna(),
                'started_on'] = degrees['completed_on'] - pd.offsets.DateOffset(years=4)
    # Convert Object type to String type to fill with "not known" string
    for col in degrees.columns:
        if degrees[col].dtype == 'O':
            degrees[col] = degrees[col].astype("string")
    # Drop the rows with no degree_type, no subject, no started_on, no completed_on.
    degrees.dropna(subset=['person_name', 'institution_uuid', 'institution_name', 'degree_type', 'subject',
                           'started_on', 'completed_on'], inplace=True)
    # Save the clean version of the dataset
    degrees.to_csv('artifacts/degrees.csv', index=False)

    # Event_appearances dataset cleaning

    logging.info('Cleaning event appearances dataset...')
    event_appearances = pd.read_csv('artifacts/event_appearances.csv', low_memory=True)
    # Remove the unneeded columns
    event_appearances.drop(['type', 'permalink', 'cb_url', 'rank', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Drop rows with missing values
    event_appearances.dropna(inplace=True)
    # Save the clean version of the dataset
    event_appearances.to_csv('artifacts/event_appearances.csv', index=False)

    # Events dataset cleaning

    logging.info('Cleaning events dataset...')
    events = pd.read_csv('artifacts/events.csv', low_memory=True)
    # Remove the unneeded columns
    events.drop(['type', 'permalink', 'cb_url', 'created_at', 'updated_at', 'logo_url'], axis=1, inplace=True)
    # missing rank will be imputed with the nominal value from the tail end of the dataset
    imput_rank(events)
    # Convert Object dtype to String Dtype to fill with "not known" string
    for col in events.columns:
        if events[col].dtype == 'O':
            events[col] = events[col].astype("string")
    # Other missing values will be imputed with "not known"
    events.fillna('not known', inplace=True)
    # Save the clean version of the dataset
    events.to_csv('artifacts/events.csv', index=False)

    # Funding rounds dataset cleaning

    logging.info('Cleaning funding rounds dataset...')
    funding_rounds = pd.read_csv('artifacts/funding_rounds.csv', low_memory=True)
    # Remove the unneeded columns
    funding_rounds.drop(['type', 'permalink', 'cb_url', 'created_at', 'updated_at', 'post_money_valuation_usd',
                         'post_money_valuation', 'post_money_valuation_currency_code', 'investor_count'], axis=1,
                        inplace=True)
    # The missing rank will be imputed with the nominal value from the tail end of the dataset
    imput_rank(funding_rounds)
    # Missing address columns will be imputed with "not known" and numerical values will be imputed with 0
    for col in funding_rounds.columns:
        if funding_rounds[col].dtype == 'O':
            funding_rounds[col] = funding_rounds[col].astype("string")
            funding_rounds[col].fillna('not known', inplace=True)
        else:
            funding_rounds[col].fillna(0, inplace=True)
    # Save the clean version of the dataset
    funding_rounds.to_csv('artifacts/funding_rounds.csv', index=False)

    # Funds dataset cleaning

    logging.info('Cleaning funds dataset...')
    funds = pd.read_csv('artifacts/funds.csv', low_memory=True)
    # Remove the unneeded columns
    funds.drop(['type', 'permalink', 'cb_url', 'rank', 'created_at',
                'updated_at'], axis=1, inplace=True)
    # Drop all rows with missing values
    funds.dropna(subset=['announced_on', 'raised_amount_usd', 'raised_amount',
                         'raised_amount_currency_code'], inplace=True)
    # Save the clean version of the dataset
    funds.to_csv('artifacts/funds.csv', index=False)

    # Investments dataset cleaning
    logging.info('Cleaning investments dataset...')
    investments = pd.read_csv('artifacts/investments.csv', low_memory=True)
    # Remove the unneeded columns
    investments.drop(['type', 'permalink', 'cb_url', 'rank', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Drop the investments rows without the names, missing funding round uuid and name
    investments.dropna(subset=['name', 'funding_round_uuid', 'funding_round_name'], inplace=True)
    # Convert Object dtype to String Dtype to fill with "not known" string
    for col in investments.columns:
        if investments[col].dtype == 'O':
            investments[col] = investments[col].astype("string")
    #  Fill all other missing values with "not known"
    investments.fillna("not known", inplace=True)
    # Save the clean version of the dataset
    investments.to_csv('artifacts/investments.csv', index=False)

    # Investments partners dataset cleaning

    logging.info('Cleaning investments partners dataset...')
    investment_partners = pd.read_csv('artifacts/investments_partners.csv', low_memory=True)
    # Remove the unneeded columns
    investment_partners.drop(['type', 'permalink', 'cb_url', 'rank', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Save the clean version of the dataset
    investment_partners.to_csv('artifacts/investments_partners.csv', index=False)

    # Investors dataset cleaning

    logging.info('Cleaning investors dataset...')
    investors = pd.read_csv('artifacts/investors.csv', low_memory=True)
    # Remove the unneeded columns
    investors.drop(['permalink', 'cb_url', 'created_at', 'updated_at', 'logo_url'], axis=1, inplace=True)
    # The rows with missing names will be dropped
    investors.dropna(subset=['name'], inplace=True)
    # The missing rank will be imputed with the nominal value from the tail end of the dataset
    imput_rank(investors)
    # Dates will be temporary cast as DateTime (returns object with fillna) to fill with 0
    investors['founded_on'] = pd.to_datetime(investors['founded_on'], errors='coerce')
    investors['closed_on'] = pd.to_datetime(investors['closed_on'], errors='coerce')
    # Fill missing values numeric value and dates will be filled with 0 and
    # other string values will be filled with "not known"
    for col in investors.columns:
        if investors[col].dtype == 'O':
            investors[col] = investors[col].astype("string")
            investors[col].fillna('not known', inplace=True)
        else:
            investors[col].fillna(0, inplace=True)
    # Save the clean version of the dataset
    investors.to_csv('artifacts/investors.csv', index=False)

    # Ipos dataset cleaning

    logging.info('Cleaning Ipos dataset...')
    ipos = pd.read_csv('artifacts/ipos.csv', low_memory=True)

    # Remove the unneeded columns
    ipos.drop(['name', 'type', 'permalink', 'cb_url', 'rank', 'created_at',
               'updated_at', 'org_cb_url'], axis=1, inplace=True)
    # Missing price currency code to be filled with USD
    ipos['money_raised_currency_code'].fillna('USD', inplace=True)
    ipos['valuation_price_currency_code'].fillna('USD', inplace=True)
    ipos['share_price_currency_code'].fillna('USD', inplace=True)
    # Missing string values (addresses etc.) filled with "not known and numeric values with 0
    for col in ipos.columns:
        if ipos[col].dtype == 'O':
            ipos[col] = ipos[col].astype("string")
            ipos[col].fillna('not known', inplace=True)
        else:
            ipos[col].fillna(0, inplace=True)
    # Save the clean version of the dataset
    ipos.to_csv('artifacts/ipos.csv', index=False)

    # Jobs dataset cleaning

    logging.info('Cleaning jobs dataset...')
    jobs = pd.read_csv('artifacts/jobs.csv', low_memory=True)
    # Remove the unneeded columns
    jobs.drop(['type', 'permalink', 'cb_url', 'rank', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Rows with missing personnel names, uuid and org_name will be dropped
    jobs.dropna(subset=['name', 'person_uuid', 'person_name', 'org_name'], inplace=True)
    jobs['title'] = jobs['title'].astype("string")
    # Rows with missing job titles will be filled with "not known"
    jobs['title'].fillna('not known', inplace=True)
    # Missing dates will be filled with 0 (will be processed to DateTime before training of model)
    jobs.fillna(0, inplace=True)
    # Save the clean version of the dataset
    jobs.to_csv('artifacts/jobs.csv', index=False)

    # Organisation parents dataset cleaning

    logging.info('Cleaning org parents dataset...')
    org_parents = pd.read_csv('artifacts/org_parents.csv', low_memory=True)
    # Remove the unneeded columns
    org_parents.drop(['permalink', 'cb_url', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Save the clean version of the dataset
    org_parents.to_csv('artifacts/org_parents.csv', index=False)

    # Organisation descriptions dataset cleaning

    logging.info('Cleaning organisation descriptions dataset...')
    organization_descriptions = pd.read_csv('artifacts/organization_descriptions.csv', low_memory=True)
    # Remove the unneeded columns
    organization_descriptions.drop(['type', 'permalink', 'cb_url', 'created_at', 'updated_at'], axis=1, inplace=True)
    # Drop the organisations without names
    organization_descriptions['name'].dropna(inplace=True)
    # Missing rank will be imputed with nominal ranks at the tail end of the dataset
    imput_rank(organization_descriptions)
    # Organisations without descriptions should be imputed with 'no description'
    organization_descriptions['description'].fillna('no description', inplace=True)
    # Save the clean version of the dataset
    organization_descriptions.to_csv('artifacts/organization_descriptions.csv', index=False)

    # Organisations dataset cleaning
    logging.info('Cleaning organisations dataset...')
    organizations = pd.read_csv('artifacts/organizations.csv', low_memory=True)
    # Remove the unneeded columns
    organizations.drop(['permalink', 'cb_url', 'created_at', 'updated_at', 'num_funding_rounds', 'total_funding_usd',
                        'total_funding', 'total_funding_currency_code', 'last_funding_on', 'logo_url', 'alias1',
                        'alias2', 'alias3', 'num_exits'], axis=1, inplace=True)
    # Convert the started_on and completed_on to DateTime data type
    organizations['founded_on'] = pd.to_datetime(organizations['founded_on'], errors='coerce')
    organizations['closed_on'] = pd.to_datetime(organizations['closed_on'], errors='coerce')
    # Drop organisations without founded_on and closed_on
    organizations.dropna(subset=['founded_on', 'closed_on'], inplace=True)
    # Fill the rows with no degree_type, no subject, no started_on, no completed_on.
    for col in organizations.columns:
        if organizations[col].dtype == 'O':
            organizations[col] = organizations[col].astype("string")
            organizations[col].fillna('not known', inplace=True)
        else:
            organizations[col].fillna(0, inplace=True)
    # Save the clean version of the dataset
    organizations.to_csv('artifacts/organizations.csv', index=False)

    # People dataset cleaning
    logging.info('Cleaning people dataset...')
    people = pd.read_csv('artifacts/people.csv', low_memory=True)
    # Remove the unneeded columns
    people.drop(['type', 'permalink', 'created_at', 'updated_at', 'cb_url', 'logo_url'], axis=1, inplace=True)
    # The missing rank will be imputed with the nominal value from the tail end of the dataset
    imput_rank(people)
    # All other missing values will be imputed with "not known"
    for col in people.columns:
        if people[col].dtype == 'O':
            people[col] = people[col].astype("string")
            people[col].fillna('not known', inplace=True)
    # Save the clean version of the dataset
    people.to_csv('artifacts/people.csv', index=False)

    # People descriptions dataset

    logging.info('Cleaning people description dataset...')
    people_descriptions = pd.read_csv('artifacts/people_descriptions.csv', low_memory=True)
    # Remove the unneeded columns
    people_descriptions.drop(['type', 'permalink', 'cb_url', 'created_at', 'updated_at'], axis=1, inplace=True)
    # The missing rank will be imputed with the nominal value from the tail end of the dataset
    imput_rank(people_descriptions)
    # Missing descriptions will be imputed with "no description"
    people_descriptions['description'].fillna('no description', inplace=True)
    # Save the clean version of the dataset
    people_descriptions.to_csv('artifacts/people_descriptions.csv', index=False)


# obj = DataIngestion()
#     obj.initiate_data_ingestion()
if __name__ == '__main__':
    clean_data()
