from src.wineqltypred.config.configuration import ConfigurationManager
from src.wineqltypred.components.model_trainer import ModelTrainer
from src.wineqltypred import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()


def run_model_trainer_pipeline():       
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e
