from Text_summary.config.configuration import ConfigurationManager
from Text_summary.components.Data_transformation import DataTransformation
from Text_summary.logging import logger

class DataTransformationTrainingPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config = data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e