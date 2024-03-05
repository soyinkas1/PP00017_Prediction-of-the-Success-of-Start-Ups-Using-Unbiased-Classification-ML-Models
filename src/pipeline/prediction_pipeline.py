import sys
import pandas as pd
from src.exception import CustomException
from src.utils.common import load_object
from src.config.configuration import ConfigurationManager
from src.entity.config_entity import PredictionPipelineConfig
from src.logger import logging


class PredictPipeline:
    def __init__(self, config: PredictionPipelineConfig):
        self.prediction_config = config

        logging.info('Prediction Configuration loaded...')
        

    def predict(self,features):
        try:
            model_path=self.prediction_config.model_path
            preprocessor_path=self.prediction_config.preprocessor_obj_path
            print("Before Loading model and preprosessor")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading model and preprosessor")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self, 
                 per_exp_at_coy_start: str,
                degree_length: str,
                yrs_since_last_funding: str,
                yrs_of_operation: str,
                institution_name: str,
                degree_type: str,
                subject: str,
                degree_is_completed: str,
                exhibitor: str,
                organizer: str,
                speaker:str, 
                sponsor:str,
                last_funding_amount: str,
                employee_count: str):

        self.per_exp_at_coy_start=per_exp_at_coy_start
        self.degree_length=degree_length
        self.yrs_since_last_funding=yrs_since_last_funding
        self.yrs_of_operation=yrs_of_operation
        self.institution_name=institution_name
        self.degree_type=degree_type
        self.subject=subject
        self.degree_is_completed=degree_is_completed
        self.exhibitor=exhibitor
        self.organizer=organizer
        self.speaker=speaker
        self.sponsor=sponsor
        self.last_funding_amount=last_funding_amount
        self.employee_count=employee_count
        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "per_exp_at_coy_start": [self.per_exp_at_coy_start],
                "degree_length": [self.degree_length],
                "yrs_since_last_funding": [self.yrs_since_last_funding],
                "yrs_of_operation": [self.yrs_of_operation],
                "institution_name": [self.institution_name],
                "degree_type": [self.degree_type],
                "subject": [self.subject],
                "degree_is_completed": [self.degree_is_completed],
                "exhibitor": [self.exhibitor],
                "organizer": [self.organizer],
                "speaker": [self.speaker],
                "sponsor": [self.sponsor],
                "last_funding_amount": [self.last_funding_amount],
                "employee_count": [self.employee_count],




            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)