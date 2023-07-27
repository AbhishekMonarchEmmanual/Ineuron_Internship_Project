import pandas as pd 
import numpy as np 
from airline.exception import airlineException
from airline.logger import logging
import os, sys
import pandas as pd 
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor,)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from airline.entity.config import *
from airline.entity.artifact import *
from sklearn.model_selection import GridSearchCV
import ast

from airline.utils import *

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig):
        try :
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise airlineException(e,sys)
        
        
    def initiate_model_trainer(self):
        
        try:
            logging.info(f"_____________MODEL TRAINING START______________")
            logging.info(f"SPlitting data into x train , x test, y train, y test")
            
            train_array = np.load(file= self.model_trainer_config.train_arr)
            test_array = np.load(file = self.model_trainer_config.test_arr)
            logging.info(f"shape of train_arr {train_array.shape}")
            logging.info(f"shape of train_arr {test_array.shape}")
                
            logging.info(f"data is loaded")
                
                
            X_train,Y_train,X_test,Y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            logging.info(f"we have splitted the data in to train and test set")
            
            logging.info(f"creating the method for using different models for machine learning")
            
            models = {
                
                "Decision Tree": DecisionTreeRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(iterations=1000, logging_level='Silent'),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'splitter':['best','random'],
                    'max_features':['sqrt','log2'],
                },
                
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
            
            logging.info(f"using each model one by one")
            
            best_models : dict=evaluate_models(X_train=X_train,Y_train= Y_train,X_test= X_test,Y_test= Y_test, models= models, param=params )
            
            logging.info(f"evaluation of the model is completed here is the best model report {best_models}")
            
            
            sorted_best_models = sorted(best_models.items(), key=lambda x: x[1]['test_score'], reverse=True)
            for rank, (model_name, model_info) in enumerate(sorted_best_models, start=1):
                print(f"Rank {rank}: {model_name} with hyperparameters: {model_info['hyperparameters']}, test score: {model_info['test_score']}")
                
            best_model_name, best_model_info = sorted_best_models[0]
            best_model = best_model_info['model']
            best_hyperparameters = best_model_info['hyperparameters']
            best_model_score = best_model_info['test_score']
            
            if best_model_score < 0.6:
                raise airlineException("No Best Method we Found")
            
            logging.info(f"Best Found model on both training and testing data set {best_model}____{best_model_name}")
            
            save_obj = save_object(
                file_path = self.model_trainer_config.model_save_path,
                obj = best_model
            )
            saved_model = save_object(
                file_path = self.model_trainer_config.save_model_obj,
                obj = best_model
            )
            logging.info(f"saving for the model is completed")
            predicted = best_model.predict(X_test)
            r2_scores = r2_score(Y_test, predicted)
            
            model_trainer_artifact = ModelTrainerArtifact(object_path=self.model_trainer_config.model_save_path, saved_model=self.model_trainer_config.save_model_obj)
            logging.info(f"Model Training Completed our Best Model : {best_model} R2_SCORE from BEST MODEL {r2_scores}")
            logging.info(f"MOdel Training Artifact is created here is the save object path {model_trainer_artifact.object_path}")
            return r2_scores, model_trainer_artifact
        except Exception as e:
            raise airlineException(e,sys)