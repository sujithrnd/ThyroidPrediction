import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as  e:
        raise CustomException(e,sys)
def evaluate_model(X_train,y_train,X_test,y_test,models):
    print('################# evaluate_model###########')


    from sklearn.model_selection import train_test_split,GridSearchCV
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.linear_model import RidgeClassifier, Lasso, ElasticNet
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
    
    try:

        report={}
        for i in range(len(models)):
            model=list(models.values()) [i]
          #TRain model
            model.fit(X_train,y_train)
            #Predict testing data
            y_test_pred=model.predict(X_test)
            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            #test_model_score=r2_score(y_test,y_test_pred)
            
            test_model_score=accuracy_score(y_test,y_test_pred)
            logging.info('model : ',model,'score :',test_model_score)
            report[list(models.keys())[i]] = test_model_score
        return report    
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj) 
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)   
    
