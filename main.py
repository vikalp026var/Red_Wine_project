from src.components.data_ingestion import DataIngestionTrainingStart
from src.components.data_validatin import DataValidationTraining
from src.components.data_transformation import DataTransformationtraining
from src.components.model_trainer import ModelTrainingStart
from src.components.model_evaluation import Model_evaluationStart





Data_ingestion=DataIngestionTrainingStart()
Data_ingestion.data_ingestion()

Data_validation=DataValidationTraining()
Data_validation.main()


Data_tarnsformation=DataTransformationtraining()
Data_tarnsformation.main()


Model_train=ModelTrainingStart()
Model_train.main()

Model_evaluation=Model_evaluationStart()
Model_evaluation.main()