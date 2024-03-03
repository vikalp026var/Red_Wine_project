import pandas as pd 
import os 
from sklearn.linear_model import ElasticNet
import joblib 
from dataclasses import dataclass
from src.config.confriguration import ConfrigurationManager
from src.entity.config_entity import ModelTrainerConfig




class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

                # Assuming self.config.target_column is a Box object or has a similar issue
        # Extract the string value of the target column name
        target_column_name = self.config.target_column['name']

        # Use the string value for dropping the column
        train_x = train_data.drop([target_column_name], axis=1)
        test_x = test_data.drop([target_column_name], axis=1)

        # Continue with your code
        train_y = train_data[[target_column_name]]

        # train_x = train_data.drop([self.config.target_column], axis=1)
        # test_x = test_data.drop([self.config.target_column], axis=1)
        # train_y = train_data([self.config.target_column])
        test_y = test_data[[target_column_name]]


        lr = ElasticNet(alpha=0.1, l1_ratio=0.2, random_state=42)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        
        
        
@dataclass
class ModelTrainingStart:
     def main(self):
          data_model_config=ConfrigurationManager()
          model_trainer_config=data_model_config.get_model_trainer_config()
          data_model=ModelTrainer(model_trainer_config)
          data_model.train()
