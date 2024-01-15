import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object 
import pandas as pd


class Predictionpipeline:
    def __ini__(self):
        pass
    def predict(self,features):
        try:
            logging.info('start prediction pipeline ')
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')
            logging.info('Load preprocessor.pkl  with preprocessor_path=',preprocessor_path)
            preprocessor=load_object(preprocessor_path)
            logging.info('Load model.pkl  with model_path=',model_path)
            model=load_object(model_path)
            logging.info('transform feautures::',type(features))
            data_scaled=preprocessor.transform(features)
            logging.info('Predict')
            pred=model.predict(data_scaled)
            logging.info('Return prediction ')
            return pred
        except Exception as e:
            logging.info('Exception occured in Prediction')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self, 
                sex :str,
                on_thyroxine:str,  
                query_on_thyroxine:str, 
                on_antithyroid_medication:str , 
                sick :str  ,
                pregnant :str  ,
                thyroid_surgery  :str ,
                I131_treatment :str  ,
                query_hypothyroid:str ,
                query_hyperthyroid:str ,
                lithium:str ,
                goitre:str ,
                tumor:str ,
                hypopituitary:str ,
                psych:str ,
                TSH_measured:str ,
                T3_measured:str ,
                TT4_measured:str ,
                T4U_measured:str,
                age:int,
                TSH:int,
                T3:int,
                TT4:int,
                T4U:int ):        
                
            self.sex =sex 
            self.on_thyroxine=on_thyroxine  
            self.query_on_thyroxine=query_on_thyroxine 
            self.on_antithyroid_medication=on_antithyroid_medication  
            self.sick   =sick   
            self.pregnant   =pregnant   
            self.thyroid_surgery=thyroid_surgery   
            self.I131_treatment=I131_treatment   
            self.query_hypothyroid=query_hypothyroid 
            self.query_hyperthyroid=query_hyperthyroid 
            self.lithium =lithium 
            self.goitre =goitre 
            self.tumor =tumor 
            self.hypopituitary=hypopituitary 
            self.psych =psych 
            self.TSH_measured=TSH_measured 
            self.T3_measured =T3_measured 
            self.TT4_measured=TT4_measured 
            self.T4U_measured=T4U_measured
            self.age=age
            self.TSH=TSH
            self.T3=T3
            self.TT4=TT4
            self.T4U=T4U  
               

    def  get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {    
				'sex':[self.sex] ,      
				'on thyroxine':[self.on_thyroxine],
				'query on thyroxine':[self.query_on_thyroxine],
				'on antithyroid medication':[self.on_antithyroid_medication],
				'sick':[self.sick],
				'pregnant':[self.pregnant],
				'thyroid surgery':[self.thyroid_surgery],
				'I131 treatment':[self.I131_treatment],
				'query hypothyroid':[self.query_hypothyroid],
				'query hyperthyroid':[self.query_hyperthyroid],
				'lithium':[self.lithium],
				'goitre':[self.goitre],
				'tumor':[self.tumor],
				'hypopituitary':[self.hypopituitary],
				'psych':[self.psych],
				'TSH measured':[self.TSH_measured],
				'T3 measured':[self.T3_measured],
				'TT4 measured':[self.TT4_measured ],
				'T4U measured':[self.T4U_measured],
                'age':[self.age],
                'TSH':[self.TSH],
                'T3':[self.T3],
                'TT4':[ self.TT4],
                'T4U':[self.T4U]                  
            }	


            df=pd.DataFrame(custom_data_input_dict)
            logging.info('Data Frame gathered')
            return df
        except Exception as e:
            logging.info('Exception occured prediction pipeline')
            raise CustomException(e,sys)
            
            
            
            
            



