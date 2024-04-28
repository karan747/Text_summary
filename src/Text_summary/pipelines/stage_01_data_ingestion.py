from Text_summary.config.configuration import ConfigurationManager
from Text_summary.components.Data_ingestion import DataIngestion
from Text_summary.logging import logger

class DataIngestionTrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_data()
        except Exception as e:
            raise e