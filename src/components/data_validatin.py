import os 
import pandas as pd 
from src.logger.logging import logging
from dataclasses import dataclass
from src.entity.config_entity import DataValidationConfig
from src.config.confriguration import ConfrigurationManager

class DataValidation:
     def __init__(self,config:DataValidationConfig):
          self.config=config
          
     def validate_all_columns(self)->bool:
          try:
               validation_status=None
               data=pd.read_csv(self.config.data_dir)
               all_cols=list(data.columns)
               all_schema=self.config.all_schema.keys()
               for col in all_cols:
                    if col not in all_schema:
                         validation_status=False
                         with open(self.config.STATUS_FILE,'w') as f:
                              f.write(f"Validation status :{validation_status}")
                    else:
                         validation_status=True
                         with open(self.config.STATUS_FILE,'w') as f:
                              f.write(f"Validation status :{validation_status}")
               return validation_status
          except Exception as e:
               raise(e)
          
@dataclass     
class DataValidationTraining:
     def main(self):
          config=ConfrigurationManager()
          data_validation_config=config.get_data_vaidation_config()
          data_validatin=DataValidation(data_validation_config)
          data_validatin.validate_all_columns()


