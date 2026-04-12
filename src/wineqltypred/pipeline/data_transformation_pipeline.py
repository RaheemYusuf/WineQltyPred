import os
from pathlib import Path
from src.wineqltypred.config.configuration import ConfigurationManager
from src.wineqltypred.components.data_transformation import DataTransformation
from src.wineqltypred.config.configuration import ConfigurationManager
from src.wineqltypred import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        status_file = ConfigurationManager().get_data_validation_config().STATUS_FILE
        try:
            with open(Path(status_file), 'r') as f:
                status_file = f.read().split(" ")[-1]
            if status_file == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            print (e)
        
def run_data_transformation_pipeline():       
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e