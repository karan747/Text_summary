from Text_summary.config.configuration import ConfigurationManager
from Text_summary.components.ModelTrainer import ModelTrainer
from Text_summary.logging import logger


class ModelTrainingPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            model_config = config_manager.get_model_trainer_config()
            model_trainer = ModelTrainer(config = model_config)
            model_trainer.train()
        except Exception as e:
            raise e