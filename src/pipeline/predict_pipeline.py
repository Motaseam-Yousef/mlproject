import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            logging.info("Before Loading")
            
            model = load_object(file_path=model_path)
            logging.info("The model was loaded")
            preprocessor = load_object(file_path=preprocessor_path)
            logging.info("The preprocessor was loaded")

            logging.info("After Loading")
            data_scaled = preprocessor.transform(features)
            logging.info("The data is scaling")
            preds = model.predict(data_scaled)
            logging.info("Model make the prediction")
            return preds

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise CustomException(str(e), sys.exc_info())

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            logging.error(f"Error occurred when converting data to DataFrame: {e}")
            raise CustomException(str(e), sys.exc_info())
