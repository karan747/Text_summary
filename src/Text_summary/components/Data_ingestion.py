import os
import urllib.request as req
import zipfile
from Text_summary.logging import logger
from Text_summary.utils.common import get_size_in_KB
from Text_summary.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.config = data_ingestion_config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = req.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"Downloaded {self.config.local_data_file} {get_size_in_KB(Path(self.config.local_data_file))}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")
    
    def extract_data(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
