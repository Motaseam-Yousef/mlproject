# put here codes for data transformation 
# 1) feature engineering
# 2) data cleaning 
# 3) categorical -> numeric
# 4) scale data

import sys
import os
import numpy as np 
import pandas as pd

from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"
            ]

            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder())
                # If you're sure about scaling after one-hot encoding, uncomment the next line
                # ("scaler", StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(str(e))

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(str(e))

if __name__ == "__main__":
    train_path = r"C:\Users\Motasem-PC\Desktop\mlproject\artifacts\test.csv"
    test_path = r"C:\Users\Motasem-PC\Desktop\mlproject\artifacts\train.csv"

    transformer = DataTransformation()
    train_arr, test_arr, preprocessor_path = transformer.initiate_data_transformation(train_path, test_path)

    logging.info(f"Processed training data shape: {train_arr.shape}")
    logging.info(f"Processed testing data shape: {test_arr.shape}")
    logging.info(f"Saved preprocessor object to: {preprocessor_path}")
