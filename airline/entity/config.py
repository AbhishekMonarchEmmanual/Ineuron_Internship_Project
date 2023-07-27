import os,sys
from airline.exception import airlineException
from airline.logger import logging
from datetime import datetime
from airline.entity.artifact import *

FILE_NAME = "airline_price_data.csv"
TRAIN_FILE_NAME = "Train_set.csv"
TEST_FILE_NAME = "Test_set.csv"
BATCH_PREDCITON_FILE = "air_price_data_test.csv"


class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        
        except Exception  as e:
            raise airlineException(e,sys)     


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="price_prediction_train"
            self.collection_name="train_data"
            self.batch_collection_name = "test_data"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.data_ingestion_batch_file = os.path.join("batch_folder", BATCH_PREDCITON_FILE)
            self.test_size = 0.3
        except Exception  as e:
            raise airlineException(e,sys)     

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise airlineException(e,sys)     

class DataTransformationConfig:
    def __init__(self, training_pipeline:TrainingPipelineConfig, data_artifacts_file_paths:DataIngestionArtifact):
        try:   
            self.preprocessor_obj_file_path = os.path.join(training_pipeline.artifact_dir, "transformed_data","preprocessor.pkl")
            self.train_data_path = data_artifacts_file_paths.train_file_path
            self.test_data_path = data_artifacts_file_paths.test_file_path
            self.transformed_train_path: str = os.path.join(training_pipeline.artifact_dir, "transformed_data","train.npy")
            self.transformed_test_path: str = os.path.join(training_pipeline.artifact_dir,"transformed_data", 'test.npy')
            self.save_model_dir = os.path.join("saved_models","preprocessor.pkl")
            self.drop_columns = ["Arrival_Time",'Date_of_Journey',"Duration", "Dep_Time","Route", "Additional_Info"]
        except Exception as e:
            raise airlineException(e,sys)

class ModelTrainerConfig:
    def __init__(self, training_pipeline: TrainingPipelineConfig, datatransformationartifact:DataTransformationArtifact):
        try :
            self.data_transformation_config = datatransformationartifact
            self.training_pipeline = training_pipeline
            self.train_arr = datatransformationartifact.train_data_arr
            self.test_arr = datatransformationartifact.test_data_arr
            self.model_save_path = os.path.join(training_pipeline.artifact_dir, "model_trainer", "model.pkl")
            self.save_model_obj = os.path.join("saved_models", "model.pkl")

            
        except Exception as e:
            raise airlineException(e,sys)
        
class BatchPredictionConfig:
    try:
        def __init__(self, training_pipeline_config: TrainingPipelineConfig, 
                     data_ingestion_config:DataIngestionConfig, 
                     data_transformation_config:DataTransformationConfig,
                     model_trainer_config:ModelTrainerConfig):
            self.training_pipeline_config = training_pipeline_config
            self.predict_file = os.path.join(training_pipeline_config.artifact_dir, "batch_prediction","predicted_batch_values.csv")
            self.batch_file = data_ingestion_config.data_ingestion_batch_file
            self.preprocess_obj = data_transformation_config.save_model_dir
            self.model_obj = model_trainer_config.save_model_obj
            self.drop_columns = ["Arrival_Time",'Date_of_Journey',"Duration", "Dep_Time","Route", "Additional_Info", "Price"]
            

    except Exception as e:
        raise airlineException(e,sys)
        
