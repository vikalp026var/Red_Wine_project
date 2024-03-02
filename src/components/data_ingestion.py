import os 
import pandas as pd 
from src.utils.common import get_size
from src.entity.config_entity import DataIngestionConfig
from src.config.confriguration import ConfrigurationManager
from src.logger.logging import logging
from dataclasses import dataclass

class DataIngestion:
     def __init__(self,config: DataIngestionConfig):
          self.config=config
          
          
     def get_data(self):
          data=pd.read_csv(self.config.source_URL,sep=',')
          
          return data
     def save_file(self,data):
          save_path = os.path.join(self.config.root_dir, 'winequality-red.csv')
          data.to_csv(save_path, index=False)
          # data.to_csv(self.config.root_dir)
@dataclass         
class DataIngestionTrainingStart:
     def data_ingestion(self):
          config=ConfrigurationManager()
          data_ingestion_config=config.get_data_ingestion_config()
          data_ingestion=DataIngestion(data_ingestion_config)
          data=data_ingestion.get_data()
          data_ingestion.save_file(data)
          logging.info("Now start ")
                    