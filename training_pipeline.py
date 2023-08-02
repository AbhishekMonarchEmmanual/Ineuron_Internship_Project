from airline.components.data_ingestion import *
from airline.components.data_transformation import *
from airline.components.model_trainer import *
from airline.components.bach_prediction import *
from airline.entity.config import *
from airline.entity.artifact import *
from airline.exception import *
from airline.logger import *
import os,sys

class TrainingPipeLine:
    def __init__(self):
        pass
    def intitate_training_pipeline(self):
        try:
            training_pipeline = TrainingPipelineConfig()
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            print(data_ingestion_artifact)


            data_transformation_config = DataTransformationConfig(training_pipeline=training_pipeline,data_artifacts_file_paths=data_ingestion_artifact)

            data_transformation = DataTrasformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact= data_transformation.initiate_data_transformation()
            print(data_transformation_artifact)

            model_trainer_config = ModelTrainerConfig(training_pipeline=training_pipeline, datatransformationartifact=data_transformation_artifact)
            model_trainer = ModelTrainer(model_trainer_config=model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            print(model_trainer_artifact)
                


#            batch_prediction_config = BatchPredictionConfig(training_pipeline_config=training_pipeline,
#                                                            data_ingestion_config=data_ingestion_config,
#                                                            data_transformation_config=data_transformation_config,
#                                                            model_trainer_config=model_trainer_config)
#
#           batch_prediction = BatchPrediction(batch_prediction_config=batch_prediction_config)
#            batch = batch_prediction.initiate_batch_prediction()'''
        except Exception as e:
            raise airlineException(e,sys)
        

  