import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols =  ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant', 'thyroid surgery',
       'I131 treatment', 'query hypothyroid', 'query hyperthyroid', 'lithium',  'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH measured',
       'T3 measured', 'TT4 measured', 'T4U measured']            
            numerical_cols =['age', 'TSH', 'T3', 'TT4', 'T4U']  
            # Define the custom ranking for each ordinal variable        

            sex = ['F','M']            
            on_thyroxine = ['f','t']
            query_on_thyroxine =['f', 't']
            on_antithyroid_medication =['f', 't']
            sick = ['f', 't']
            pregnant = ['f', 't']
            thyroid_surgery = ['f', 't']
            I131_treatment = ['f', 't']
            query_hypothyroid=['f', 't']
            query_hyperthyroid=['f', 't']
            lithium=['f', 't']
            goitre=['f', 't']
            tumor=['f', 't']
            hypopituitary=['f', 't']
            psych=['f', 't']
            TSH_measured=['f', 't']
            T3_measured=['f', 't']
            TT4_measured=['f', 't']
            T4U_measured=['f', 't']    
                     
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[('imputer',SimpleImputer(strategy='median')), ('scaler',StandardScaler()) ]

            )
            # Categorigal Pipeline                     
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[
                   sex, on_thyroxine  ,  query_on_thyroxine , on_antithyroid_medication ,  sick  ,   pregnant  ,            thyroid_surgery  ,            I131_treatment  ,            query_hypothyroid,            query_hyperthyroid,            lithium,            goitre,            tumor,            hypopituitary,            psych,            TSH_measured,            T3_measured,            TT4_measured,            T4U_measured
                    ])),                    
                 ('scaler',StandardScaler())
                ]

            )
            logging.info('Pipeline Initiated 22')
            preprocessor=ColumnTransformer([ ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)          
            ])   
            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)
        
    def initaite_data_transformation(self,train_path,test_path):
        logging.info('ini data transformation start 00')
        try:
            # Reading train and test data
            logging.info('ini data transformation start ')
            train_df = pd.read_csv(train_path)
            logging.info('ini data transformation start :',type(train_df))
            test_df = pd.read_csv(test_path)
            logging.info('ini data transformation start 2')
            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')
            
            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()
            target_column_name = 'binaryClass'            
            train_df = train_df.reset_index(drop=True)
            test_df = test_df.reset_index(drop=True)
            drop_columns = [target_column_name]

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)

            target_feature_test_df=test_df[target_column_name]           
            logging.info('input_feature_test_df shape ',input_feature_test_df.shape) 
                      
            ## Trnasformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            logging.info('ini data transformation start 8**',input_feature_train_arr)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            logging.info("Applying preprocessing object on training and testing datasets.")    

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise CustomException(e,sys)