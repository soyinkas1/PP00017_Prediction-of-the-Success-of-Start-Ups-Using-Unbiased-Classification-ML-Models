import sys
import pandas as pd
from src.exception import CustomException
from src.utils.common import load_object
from src.config.configuration import ConfigurationManager
from src.entity.config_entity import PredictionPipelineConfig
from src.logger import logging





class PredictPipeline:
    def __init__(self, config: PredictionPipelineConfig):    
        """
        configures the attributes of each instance of the class
        Arg: 
            Config: configuration of the attribute (configBox)
        """
        self.prediction_config = config

        logging.info('Prediction Configuration loaded...')
        

    def predict(self,features):
        """
        Carries out prediction on the features provided
        Arg: 
            Features: Features from web app on which prediction is done (DataFrame)
        """
  
        try:
            model_path=self.prediction_config.model_path
            preprocessor_path=self.prediction_config.preprocessor_obj_path
            print("Before Loading model and preprosessor")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading model and preprosessor")

            
            data_scaled=preprocessor.transform(features)
            data_scaled.shape
            preds=model.predict(data_scaled)
            return preds
             # Load the preprocessor and fit it with features
            print(features.shape)
            # preprocessor_path = self.prediction_config.preprocessor_obj_path
            # preprocessor = load_object(file_path=preprocessor_path)
            # preprocessor.fit(features)

            # # Load the model
            # model_path = self.prediction_config.model_path
            # model = load_object(file_path=model_path)
            
            # # Transform features using the fitted preprocessor
            # data_scaled = preprocessor.transform(features)
            print(data_scaled.shape)
            
            # # Make predictions
            # preds = model.predict(data_scaled)
            
            # return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self, 
                 yrs_of_operation: int,
        yrs_since_last_funding: int,
        degree_length: int,
        per_exp_at_coy_start: int,
        sponsor: int,
        speaker: int,
        organizer: int,
        exhibitor: int,
        employee_count: int,
        total_funding_usd: int,
        organization_description: str,
        people_description: str,
        status: str,
        category_list: str,
        category_groups_list: str,
        primary_role: str,
        gender: str,
        featured_job_title: str,
        institution_name: str,
        degree_type: str,
        subject: str,
        degree_is_completed: str):

        self.yrs_of_operation=yrs_of_operation
        self.yrs_since_last_funding=yrs_since_last_funding
        self.degree_length=degree_length
        self.per_exp_at_coy_start=per_exp_at_coy_start
        self.sponsor=sponsor
        self.speaker=speaker
        self.organizer=organizer
        self.exhibitor=exhibitor
        self.employee_count=employee_count
        self.total_funding_usd=total_funding_usd
        self.organization_description=organization_description
        self.people_description=people_description
        self.status=status
        self.category_list=category_list
        self.category_groups_list=category_groups_list
        self.primary_role=primary_role
        self.gender=gender
        self.featured_job_title=featured_job_title
        self.institution_name=institution_name
        self.degree_type=degree_type
        self.subject=subject
        self.degree_is_completed=degree_is_completed
        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "per_exp_at_coy_start": [self.per_exp_at_coy_start],
                "yrs_of_operation": [self.yrs_of_operation],
                "degree_length": [self.degree_length],
                "yrs_since_last_funding": [self.yrs_since_last_funding],
                "per_exp_at_coy_start": [self.per_exp_at_coy_start],
                "sponsor": [self.sponsor],
                "speaker": [self.speaker],
                "organizer": [self.organizer],
                "exhibitor": [self.exhibitor],
                "employee_count": [self.employee_count],
                "total_funding_usd": [self.total_funding_usd],
                "organization_description": [self.organization_description],
                "people_description": [self.people_description],
                "status": [self.status],
                "category_list": [self.category_list],
                "category_groups_list": [self.category_groups_list],
                "primary_role": [self.primary_role],
                "gender": [self.gender],
                "featured_job_title": [self.featured_job_title],
                "institution_name": [self.institution_name],
                "degree_type": [self.degree_type],
                "subject": [self.subject],
                "degree_is_completed": [self.degree_is_completed]
                

            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)