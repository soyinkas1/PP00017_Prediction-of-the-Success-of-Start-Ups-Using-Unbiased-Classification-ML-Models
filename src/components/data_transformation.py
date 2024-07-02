# Import the required external libraries
import pandas as pd
import numpy as np
from datetime import date
import sys
import os
import warnings
import dill
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Import the required internal classes and methods
from src.entity.config_entity import DataTransformationConfig, DataCleaningConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.common import save_object, process_batch, process_in_batches, download_blob_to_df, upload_dataframe_to_blob


# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class DataTransformation:
    """"
    This class is transform and carry out feature engineering to produce the final dataset for modelling
    """
    def __init__(self, config: DataTransformationConfig, clean_data_config: DataCleaningConfig):
        self.transform_config = config
        self.clean_data_config = clean_data_config

    logging.info("Data transformation configuration done......")

    def data_transformation(self):
        
        try:
            df = pd.read_csv(self.clean_data_config.clean_backbone_local_data_file,
                            parse_dates=self.transform_config.columns_to_parse_dates)
            
            logging.info("Data uploaded from data cleaning stage......")
            logging.info("Data transformation started......")
            # The following features should be filled with 'not known' and 'False' respectively  
            df[self.transform_config.institution_name].fillna('not known',inplace=True)
            df[self.transform_config.degree_type].fillna('not known',inplace=True)
            df[self.transform_config.subject].fillna('not known',inplace=True)
            df[self.transform_config.degree_is_completed].fillna('False',inplace=True, downcast={'object':bool})

            # The dates will be filled with current date so that the derived dates from these will be zero (0)
            for col in df.columns:
                if df[col].dtype == 'O':
                    df[col].fillna('not known',inplace=True)
                elif not df[col].dtype == '<M8[ns]':
                    df[col].fillna(0,inplace=True)
                elif df[col].dtype == '<M8[ns]':
                    df[col].fillna(np.datetime64(date.today()), inplace=True)

            # Cast the data type for 'exhibitor', 'organizer', 'speaker', 'sponsor' from float to int
            df[self.transform_config.exhibitor] = df[self.transform_config.exhibitor].astype(np.int64)
            df[self.transform_config.organizer] = df[self.transform_config.organizer].astype(np.int64)
            df[self.transform_config.speaker] = df[self.transform_config.speaker].astype(np.int64)
            df[self.transform_config.sponsor] = df[self.transform_config.sponsor].astype(np.int64)
            df[self.transform_config.degree_is_completed] = df[self.transform_config.degree_is_completed].astype(bool)
            logging.info("Casting data types......")
            # drop all all rows with duplicate values across all columns.
            df.drop_duplicates(keep='first', inplace=True)

           
            logging.info("Feature Engineering...creating new columns...")
            # Create column for the years of experience of personnel at the founding of the company
            df.loc[df['founded_on'] < df['degree_completed_on'] , 'founded_on'] = df['degree_completed_on']
            df['per_exp_at_coy_start'] = df['founded_on'] - df['degree_completed_on']
            df['per_exp_at_coy_start'] = (df['per_exp_at_coy_start'].dt.days / 365).astype(np.int64)
                             
            # Create a column for the Length of degree of personnel
            df[self.transform_config.degree_length] = (df[self.transform_config.degree_completed_on] - df[self.clean_data_config.degree_started_on])
            # Convert the negative values to 0 days
            df[self.transform_config.degree_length] = df[self.transform_config.degree_length].apply(
                lambda x: x if(x/pd.Timedelta(hours=1) > 0) else (pd.Timedelta(seconds=0)) )
            # Convert the days to years 
            df[self.transform_config.degree_length] = ((df[self.transform_config.degree_length].dt.days)/365).astype(np.int64)

            # Create a column for the years since the last funding received by the organisation
            df[self.transform_config.yrs_since_last_funding] = np.datetime64(date.today()) - df[self.transform_config.last_funding_on]
            # Convert the negative values to 0 days
            df[self.transform_config.yrs_since_last_funding] = df[self.transform_config.yrs_since_last_funding].apply(
                lambda x: x if(x/pd.Timedelta(hours=1) > 0) else (pd.Timedelta(seconds=0)) )
            # Covert the days to years 
            df[self.transform_config.yrs_since_last_funding] = ((df[self.transform_config.yrs_since_last_funding].dt.days)/365).astype(np.int64)

            # Create a column for the years of operation of the organisation
            df[self.transform_config.yrs_of_operation] = df[self.transform_config.closed_on] - df[self.transform_config.founded_on] 
            # Convert the negative values to 0 days
            df[self.transform_config.yrs_of_operation] = df[self.transform_config.yrs_of_operation].apply(
                lambda x: x if(x/pd.Timedelta(hours=1) > 0) else (pd.Timedelta(seconds=0)) )
            # Convert the days to years 
            df[self.transform_config.yrs_of_operation] = ((df[self.transform_config.yrs_of_operation].dt.days)/365).astype(np.int64)
            
            logging.info("Dropping unneeded columns......")
            # Drop the columns that are no longer required
            df.drop(self.transform_config.columns_to_drop,axis=1,inplace=True)

            # rearrange the dataset features
            df = df[self.transform_config.columns_rearrangement]

            # Reset the index of DataFrame
            df.reset_index(drop=True, inplace=True)

            logging.info("Defining success column......")
            df.loc[df['employee_count'] >= 1000, 'success'] = 1

            # Set the organisations with years of operation of 20 years and above as successful
            df.loc[df['yrs_of_operation'] >= 20, 'success'] = 1

            # Create a DataFrame of organisation with one or more rows as success = 1
            suc_df = pd.DataFrame(df.groupby(self.transform_config.uuid)[self.transform_config.success].
                                sum()[df.groupby(self.transform_config.uuid)[self.transform_config.success].sum()>0])
            
            # Update all rows of these organisations to success = 1
            matching_uuids = df['uuid'].isin(suc_df.index)

            #  Update the 'success' column in matching rows to 1
            df.loc[matching_uuids, 'success'] = 1
            
            # drop company ID
            df.drop('uuid',axis=1, inplace=True)

            # Save the updated final dataset at this stage
            df.to_csv(self.transform_config.transformed_data_local_data_file, index=False)

            logging.info("Saving transformed dataset......")

            logging.info("Splitting transformed data......")
            # Split the dataset into Training, Validation and Test sets in 60, 20, 20
            train, validate, test = np.split(df.sample(frac=1), [int(self.transform_config.train_percent*len(df)), 
                        int((self.transform_config.train_percent+self.transform_config.validate_percent)*len(df))])
            
            
           # Create a list of feature categorisations
            num_features = self.transform_config.num_features
            text_feature_o =  self.transform_config.text_feature_o
            text_feature_p = self.transform_config.text_feature_p
            cat_features = self.transform_config.cat_features
            
            logging.info("Data pipeline definition......")
            # Define individual pipelines
            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scalar', StandardScaler())  
                ]
            )

            text_pipeline = Pipeline(
                steps=[
                    ('vectorizer', TfidfVectorizer(stop_words="english"))
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='constant', fill_value='not known')),
                    ('one_hot', OneHotEncoder(handle_unknown='ignore')),
                    ('scalar', StandardScaler(with_mean=False))
                ]
            )

            # Create the preprocessing pipeline
            preprocessor = ColumnTransformer(
            transformers=[
                ("text_o", text_pipeline, text_feature_o),
                ("text_p", text_pipeline, text_feature_p),
                ("num", num_pipeline, num_features),
                ("cat", cat_pipeline, cat_features)
            ],remainder='passthrough'  
            )


            # Spilt the train, validate and test data into features and labels before applying the preprocessor
            X_train = train.drop('success', axis=1)
            y_train = train['success']

            X_val = validate.drop('success', axis=1)
            y_val = validate['success']

            X_test = test.drop('success', axis=1)
            y_test = test['success']


         
            # Fit and transform the training input features data
            X_train = preprocessor.fit_transform(X_train)

            save_object(self.transform_config.preprocessor_obj_path, preprocessor)
            logging.info("Saved preprocessor ......")

            print(f'transformed shape of X_train:{X_train.shape}')
            # Transform the Validation input features data
            X_val = preprocessor.transform(X_val)
            print(f'transformed shape of X_val:{X_val.shape}')
            # Transform the Test input features data set
            X_test = preprocessor.transform(X_test)
            print(f'transformed shape of X_test:{X_val.shape}')
            
            # Combine the X and y of the train, validate and test dataset and save to complete the transformation
            
           
          

                # Train dataset
            # Convert to DataFrame and reset index
            y_train_df = y_train.to_frame()
            y_train_df.reset_index(drop=True, inplace=True)

            # Combine X_train and y_train_df
            process_in_batches(X_train, y_train_df,3000, self.transform_config.train_data_local_data_file )

            # train_df = pd.concat([pd.DataFrame(X_train.todense()), y_train_df], axis=1)

            # # Save to CSV file
            # train_df.to_csv(self.transform_config.train_data_local_data_file, index=False)
        
            logging.info("Saving final train dataset......")
            
                # Validation dataset
            # Convert to DataFrame and reset index
            y_val_df = y_val.to_frame()
            y_val_df.reset_index(drop=True, inplace=True)

            # Combine X_val and y_val_df
            process_in_batches(X_val, y_val_df,3000, self.transform_config.validate_data_local_data_file )

            # val_df = pd.concat([pd.DataFrame(X_val.todense()), y_val_df], axis=1)

            # # Save to CSV file
            # val_df.to_csv(self.transform_config.validate_data_local_data_file, index=False)
            
            logging.info("Saving final validate dataset......")


                # Test dataset
            # Convert to DataFrame and reset index
            y_test_df = y_test.to_frame()
            y_test_df.reset_index(drop=True, inplace=True)

            # Combine X_test and y_test_df
            process_in_batches(X_test, y_test_df,10000, self.transform_config.test_data_local_data_file )
            
            
            # test_df = pd.concat([pd.DataFrame(X_test.todense()), y_test_df], axis=1)

            # # Save to CSV file
            # test_df.to_csv(self.transform_config.test_data_local_data_file, index=False)

            logging.info("Saving final test dataset......")

            logging.info("Data transformation completed......")
        
        except Exception as e:
            raise CustomException(e, sys)


