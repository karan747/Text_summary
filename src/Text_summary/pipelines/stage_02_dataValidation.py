from Text_summary.config.configuration import ConfigurationManager
from Text_summary.components.Data_validation import DataValidation
from Text_summary.logging import logger

class DataValidationTrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation_config = DataValidation(data_validation_config=data_validation_config)
            data_validation_config.validate_all_fiies_exist()
        except Exception as e:
            raise e