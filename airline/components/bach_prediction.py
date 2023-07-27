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


class BatchPrediction:
    def __init__(self, batch_prediction_config:BatchPredictionConfig):
        self.batch_prediction_config = batch_prediction_config
        
    def initiate_batch_prediction(self):
        
        model = load_object(self.batch_prediction_config.model_obj)
        preprocess_obj = load_object(self.batch_prediction_config.preprocess_obj)
        
        df_eng= feature_eng(df_path= self.batch_prediction_config.batch_file , col = self.batch_prediction_config.drop_columns)
        df_array = preprocess_obj.transform(df_eng)
        y_pred = model.fit(df_array)
        
        
        
        
        print(f"df_eng shape and columns {df_eng.shape, df_eng.columns}")
        print(f"df_array shape : {df_array.shape}")
        
        
