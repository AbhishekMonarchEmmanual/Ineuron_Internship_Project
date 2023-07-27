from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str
    batch_store_dir:str
    
@dataclass

class DataTransformationArtifact:
    train_data_arr:str
    test_data_arr: str 
    preprocess_obj:str
    saved_obj : str

@dataclass
class ModelTrainerArtifact:
    object_path:str
    saved_model : str
    

