import pandas as pd 
import numpy as np 
from airline.exception import airlineException
from airline.logger import logging
from airline.mongo_config import *
from airline.entity.config import *
import os, sys
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from airline.entity.artifact import *
from airline.entity.config import *
from dataclasses import dataclass
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import dill

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise airlineException(e, sys)
    
    
def feature_eng(df_path, col ):   
        try : 
            logging.info(f"_____________DATA FEATURE ENGINEERING BEGINS for {df_path}____________________")
            logging.info(f"WE ARE GOING TO CREATE DATAFRAME for {df_path}")
            train_df = pd.read_csv(df_path)
            logging.info(f"{train_df.head(5)}")
           
        
            logging.info(f"DATA FRAMES ARE BUILT NOW for {df_path} WE ARE GOING TO PERFROM FEATURE ENGINEERING")
            logging.info(f"dataframe {train_df.columns} and here is the shape of the data_frame {train_df.shape} for {df_path}")
           
            logging.info(f"Dropping NA values dataframe {train_df.isnull().sum()}")
            train_df.dropna(inplace=True)
            logging.info(f"dropped na value in {df_path} here are the {train_df.shape} and {train_df.columns} ")
            
            
            logging.info(f" extracting day and month in dataframe")
            train_df['Date_of_Journey'] = pd.to_datetime(train_df.Date_of_Journey, format='%d/%m/%Y')
            #adding new columns(Journey_day, Journey_month, Journey_year) out of column(Date_of_Journey)
            train_df['Journey_day'] = train_df['Date_of_Journey'].dt.day
            #extracting monthtrain_df
            train_df['Journey_month'] = train_df['Date_of_Journey'].dt.month
            logging.info(f"extraction of month and day of journey completed")
            logging.info(f"{train_df.Date_of_Journey.dtype} for the following {df_path} and here are the list of columns {train_df.columns} and shape {train_df.shape}")
            
            
            
            ########converting train arrival time to date time 
            logging.info(f"converting 'Arrival_Time' to 'datetime' for {df_path}")
            train_df['Arrival_Time'] = pd.to_datetime(train_df.Arrival_Time)
            train_df['Arrival_hour'] = train_df['Arrival_Time'].dt.hour
            #extracting Arrival minute
            train_df['Arrival_minute'] = train_df['Arrival_Time'].dt.minute
            
            logging.info(f"converted and created the column for arrival time")
            logging.info(f"{df_path} data frame has follwoing columns {train_df.columns} and following shape {train_df.shape} after extraction of arrival time")
            ######creating the same in test df
            
            
            
            ###### creating for dep_time
            logging.info(f"converting 'departure_Time' to 'datetime' for df for {df_path}")
            train_df['Dep_Time'] = pd.to_datetime(train_df.Dep_Time)
            train_df['Dep_hour'] = train_df['Dep_Time'].dt.hour
            #extracting Arrival minute
            train_df['Dep_minute'] = train_df['Dep_Time'].dt.minute
            logging.info(f"converted and created the column for dep time")
            logging.info(f"{df_path} data frame has follwoing columns {train_df.columns} and following shape {train_df.shape} after extraction of departure time")
            ######creating the same in test df
           
            
            #Now splitting duration column to extract information for train df 
            
            logging.info(f"beggining the extraction of information from dataframe from Duration column for {df_path}")
            
            
            duration = list(train_df["Duration"])

            for i in range(len(duration)):
                if len(duration[i].split()) != 2:    # Check if duration contains only hour or mins
                    if "h" in duration[i]:
                        duration[i] = duration[i].strip() + " 0m"   # Adds 0 minute #why strip is used here?
                    else:
                        duration[i] = "0h " + duration[i]           # Adds 0 hour

            duration_hours = []
            duration_mins = []
            for i in range(len(duration)):
                duration_hours.append(int(duration[i].split(sep = "h")[0]))    # Extract hours from duration
                duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1]))
            train_df['Duration_hours'] = duration_hours
            train_df['Duration_minutes'] = duration_mins
            logging.info(f"{df_path} dataframe has columns {train_df.columns} and shape : {train_df.shape}")
            
            logging.info(f"{df_path} dataframe column dropping has started")
            drop_column(df=train_df, col= col)
            logging.info(f"after dropping columns from {df_path} data frame here are the list of column : {train_df.columns} and shape of the data_frame {train_df.shape}")
            logging.info(f" data type of each column is as follows {train_df.dtypes} ")
            logging.info(f"dropped the columns required to be dropped after all the extraction of information list of dropped columns from {col}")
            logging.info(f"Ending the Feature Engineering")
            return train_df 
        except Exception as e:
            raise airlineException(e,sys)
        
def evaluate_models(X_train, Y_train,X_test,Y_test,models,param):
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():
            para = param[model_name]

            gs = GridSearchCV(model, para, cv=3)

            gs.fit(X_train, Y_train)

            best_model = gs.best_estimator_
            best_hyperparameters = gs.best_params_

            best_model.fit(X_train, Y_train)

            Y_train_pred = best_model.predict(X_train)
            Y_test_pred = best_model.predict(X_test)

            train_model_score = r2_score(Y_train, Y_train_pred)
            test_model_score = r2_score(Y_test, Y_test_pred)

            report[model_name] = test_model_score
            best_models[model_name] = {
                "model": best_model,
                "hyperparameters": best_hyperparameters,
                "test_score": test_model_score
            }

        return best_models

    except Exception as e:
        raise airlineException(e, sys)
        
def drop_column(df: pd.DataFrame,col:list):
    try:
        
        df = df
        col = col
        
        df.drop(col, axis = 1, inplace=True)
        
    except Exception as e:
        raise airlineException(e,sys)
    

  
def get_data_transformer_object():
    """_summary_
    use for transofrming the data frame for prediction

    Returns:
        scaling obj: it will scale and transform our data based on the pipeline we have created 
    """
    try:
    
        one_hot_encoding_columns =["Airline","Source","Destination"] 
        label_encoding_columns = ["Total_Stops"]
        scaling_columns= ['Journey_day','Journey_month','Arrival_hour','Arrival_minute','Dep_hour','Dep_minute','Duration_hours','Duration_minutes']
        one_hot_encoding_pipeline = Pipeline(
            
              steps=[
                
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ]
        )
        
        label_encoding_pipeline= Pipeline(
      
            steps=[
                
                ("Label_encoder",OrdinalEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ]
        )
        scaling_pipeline= Pipeline(
      
            steps=[
                
                
                ("scaler", StandardScaler(with_mean=False))
            ]
        )
        preprocessor = ColumnTransformer(
            [
                ("one_hot_encoding_pipeine", one_hot_encoding_pipeline,one_hot_encoding_columns),
                ("label_encoding_piplines",label_encoding_pipeline,label_encoding_columns),
                ("scaling_pipeline", scaling_pipeline, scaling_columns)
                
            ]
        )
 
        return preprocessor
 
    except Exception as e:
        raise airlineException(e,sys)
    

def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise airlineException(e, sys)

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise e


def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise airlineException(e, sys) from e


def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise airlineException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise airlineException(e, sys) from e

def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise airlineException(e, sys)
    