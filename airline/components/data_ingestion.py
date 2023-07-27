
from airline import utils
from airline.entity.config import *
from airline.entity.artifact import *
from airline.exception import airlineException
from airline.logger import logging
import os,sys
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self,data_ingestion_config: DataIngestionConfig ):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise airlineException(e, sys)

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")
            #Exporting collection data as pandas dataframe
            df:pd.DataFrame  = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name, 
                collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"{df.shape}")
            df1:pd.DataFrame= utils.get_collection_as_dataframe(
                database_name = self.data_ingestion_config.database_name,
                collection_name = self.data_ingestion_config.batch_collection_name
            )
            logging.info(df.shape)
            logging.info(df.columns)
            logging.info(df1.shape)
            logging.info(df1.columns)

            logging.info("Save data in feature store")
            

            #replace na with Nan
            df.replace(to_replace="na",value=np.NAN,inplace=True)

            #Save data in feature store
            logging.info("Create feature store folder if not available")
            #Create feature store folder if not available
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)
            logging.info("Save df to feature store folder")
            #Save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)
            
            #replace na with Nan
            df.replace(to_replace="na",value=np.NAN,inplace=True)

            #Save data in feature store
            logging.info("Create batch prediction store folder if not available")
            #Create feature store folder if not available
            batch_store_dir = os.path.dirname(self.data_ingestion_config.data_ingestion_batch_file)
            os.makedirs(batch_store_dir,exist_ok=True)
            logging.info("Save batch df to feature store folder")
            #Save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.data_ingestion_batch_file,index=False,header=True)


            logging.info("split dataset into train and test set")
            #split dataset into train and test set
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size, random_state=3)
            
            logging.info("create dataset directory folder if not available")
            logging.info(f"train-df shape {train_df.shape}")
            logging.info(f"column in train_df {train_df.columns}")
            logging.info(f"test_df shape {test_df.shape}")
            logging.info(f"column in test_df {test_df.columns}")
            #create dataset directory folder if not available
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            logging.info("Save df to feature store folder")
            #Save df to feature store folder
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)
            
            #Prepare artifact

            data_ingestion_artifact = DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path, 
                test_file_path=self.data_ingestion_config.test_file_path,
                batch_store_dir= self.data_ingestion_config.data_ingestion_batch_file)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise airlineException(error_message=e, error_detail=sys)



        
