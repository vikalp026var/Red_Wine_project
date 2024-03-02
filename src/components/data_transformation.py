import os 
import pandas as pd
from sklearn.model_selection import train_test_split 
from src.logger.logging import logging
from src.entity.config_entity import DataTransformationConfig
from dataclasses import dataclass
from src.config.confriguration import ConfrigurationManager



class DataTransformation:
     def __init__(self,config:DataTransformationConfig):
          self.config=config
          
     def train_test_splitting(self):
          data=pd.read_csv(self.config.data_path)
          train,test=train_test_split(data)
          train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
          test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
          
          
          
@dataclass
class DataTransformationtraining:
     def __init__(self):
          pass
     def main(self):
          try:
               config=ConfrigurationManager()
               data_tranformation_config=config.get_data_tansformation_config()
               data_tranformation=DataTransformation(config=data_tranformation_config)
               data_tranformation.train_test_splitting()
          except Exception as e:
               raise e 