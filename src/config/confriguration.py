from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig
from src.logger.logging import logging


class ConfrigurationManager:
     def __init__(self,
                  config_filepath=CONFIG_PATH,
                  params_filepath=PARAMS_PATH,
                  schema_filepath=SCHEMA_PATH
                  ):
          self.config=read_yaml(config_filepath)
          self.params=read_yaml(params_filepath)
          self.schema=read_yaml(schema_filepath)
          create_directories([Path(self.config['artifacts_root'])])
          
     def get_data_ingestion_config(self)->DataIngestionConfig:
          config=self.config.data_ingestion
          create_directories([Path(config['root_dir'])])
          data_ingestion_config=DataIngestionConfig(
               root_dir=config.root_dir,
               source_URL=config.source_URL
          )
          return data_ingestion_config
          
     def get_data_vaidation_config(self)->DataValidationConfig:
          config=self.config.data_validation
          schema=self.schema.COLUMNS
          create_directories([Path(config['root_dir'])])
          logging.info("Root dir is make ")
          data_validation_config=DataValidationConfig(
               root_dir= config.root_dir,
               data_dir= config.data_dir,
               STATUS_FILE= config.STATUS_FILE,
               all_schema=schema,
               
          )
          logging.info("....")
          return data_validation_config
          
          
          
     def get_data_tansformation_config(self)->DataTransformationConfig:
          config=self.config.data_transformation
          create_directories([Path(config['root_dir'])])
          data_transformation_config=DataTransformationConfig(
               root_dir=config.root_dir,
               data_path=config.data_path
          )
          return data_transformation_config
     
     def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            # alpha = params.alpha,
            # l1_ratio = params.l1_ratio,
            target_column = schema
            
        )

        return model_trainer_config
   
   
     def get_model_evaluation_config(self)-> ModelEvaluationConfig:
          config=self.config.model_evaluation
          params=self.params.ElasticNet
          schema=self.schema.TARGET_COLUMN
          create_directories([config.root_dir])
          model_evaluation_config=ModelEvaluationConfig(
               root_dir=config.root_dir,
               test_data_path=config.test_data_path,
               model_path=config.model_path,
               all_params=params,
               metric_file_name=config.metric_file_json,
               target_column=schema.name
          )
          return model_evaluation_config