import pandas as pd 
import numpy as np 
from airline.exception import airlineException
from airline.logger import logging
import os, sys
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from airline.entity.config import *
from airline.entity.artifact import *
from airline.utils import *
import dill

class DataTrasformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifact:DataIngestionArtifact):
        
        
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise airlineException(e,sys)
        
    def initiate_data_transformation(self):
        
        try : 
            logging.info(f"__________DATA TRANSFORMATION BEGINS____________")
            
            train_df = feature_eng(df_path=self.data_ingestion_artifact.train_file_path, col=self.data_transformation_config.drop_columns)
            test_df = feature_eng(df_path=self.data_ingestion_artifact.test_file_path, col=self.data_transformation_config.drop_columns)
            logging.info(f"{train_df.shape} and column {train_df.columns}")
            logging.info(f"{test_df.shape} and columns {test_df.columns}")
            
            logging.info(f"concatenate both train and test df since we need to match column number in both after preprocessing")
            
            
            
            
            
            
            # after preprocessing creating train and test array
            TARGET_COLUMN = "Price"
            logging.info(f"creating train and test feature data frame and dropping Price column from both data frame")
            
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            logging.info(f"input train feature df {input_feature_train_df.columns}, and its shape {input_feature_train_df.shape}")
            logging.info(f"input train feature df  shape {input_feature_train_df.shape}")
            logging.info(f"target feature df {target_feature_train_df.head(5)} and {target_feature_train_df.shape}")
  
  
            logging.info(f"starting to create input and target feature on test data frame")
            
            # after preprocesing creating input test and target feature test
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            logging.info(f"input test feature {input_feature_test_df.columns}")
            logging.info(f"input feature test df shape {input_feature_test_df.shape}")
            logging.info(f"target test feature test df {target_feature_test_df.head(5)}")
            logging.info(f"target test feature test df shape {target_feature_test_df.shape}")
            
            logging.info(f"Starting the preprocessing of our dataset")
            
            combined_df = pd.concat([input_feature_train_df, input_feature_test_df], axis=0)
            
            preprocessing_obj = get_data_transformer_object()
            
            
            pre_obj= preprocessing_obj.fit(combined_df)
            
            input_feature_train_arr= pre_obj.transform(input_feature_train_df)
            
            input_feature_test_arr= pre_obj.transform(input_feature_test_df)
            logging.info(f"shape of  input_feature_train_arr : {input_feature_train_arr.shape}")
            logging.info(f"shape of input_feature_test_arr : {input_feature_test_arr.shape}")
            
            logging.info(f"shape of test_arr {np.array(target_feature_train_df).shape}")
            logging.info(f"shape of test_arr {np.array(target_feature_test_df).shape}")
            
            logging.info(f"_______Combining array__________")
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info(f"shape of train_arr {train_arr.shape}")
            logging.info(f"shape of test_arr {test_arr.shape}")
            
            
           
            
            logging.info(f"_________PREPARING FOR SAVING OBJECT AND 'dill' FILE_____________")
            
            save_object(
                file_path= self.data_transformation_config.preprocessor_obj_file_path,
                obj=pre_obj
            )
            save_object(
                file_path= self.data_transformation_config.save_model_dir,
                obj=pre_obj
            )
            
            logging.info(f"_________SAVING NUMPY ARRAY_____________")
            np.save(self.data_transformation_config.transformed_train_path, train_arr)
            np.save(self.data_transformation_config.transformed_test_path, test_arr)
            
            logging.info(f"_________PREPARING DATA TRANSFORMATION ARTIFACT_____________")
            
            data_transformation_artifact= DataTransformationArtifact( 
                train_data_arr=self.data_transformation_config.transformed_train_path, 
                test_data_arr=self.data_transformation_config.transformed_test_path,
                preprocess_obj=self.data_transformation_config.preprocessor_obj_file_path,
                saved_obj=self.data_transformation_config.save_model_dir
                
                )
            
            logging.info(f"_______DATA TRANSFORMATION COMPLETE______")
            logging.info(f"object path : {data_transformation_artifact.preprocess_obj}, train arr path : {data_transformation_artifact.train_data_arr}, test arr path {data_transformation_artifact.test_data_arr}")
            
            
            return  data_transformation_artifact
            
        except Exception as e:
            raise airlineException(e,sys)       
                   
          
            
          
            
            
            
            
            
            
          
            
          
            


        except Exception as e:
            raise airlineException(e,sys)
