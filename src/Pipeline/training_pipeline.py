# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# from src.Components.data_ingestion import DataIngestion
# from src.Components.data_transformation import DataTransformation
# from src.Components.model_trainer import ModelTrainer
# from src.exception import CustomException

# class TrainingPipeline:
#     def start_data_ingestion(self):
#         try:
#             data_ingestion = DataIngestion()
#             feature_store_file_path = data_ingestion.initiate_data_ingestion()
#             return feature_store_file_path
#         except Exception as e:
#             raise CustomException(e,sys)

    
#     def start_data_transformation(self,feature_store_file_path):
#         try:
#             data_transformation = DataTransformation(feature_store_file_path=feature_store_file_path)
#             train_arr,test_arr,preprocessor_path = data_transformation.initaiate_data_transformation()
#             return train_arr,test_arr,preprocessor_path

#         except Exception as e:
#             raise CustomException(e,sys)

    
#     def start_model_trianing(self,train_arr,test_arr):
#         try:
#             model_trainer = ModelTrainer()
#             model_score = model_trainer.initiate_model_trainer(
#                 train_arr,test_arr
#             )
#             return model_score

#         except Exception as e:
#             raise CustomException(e,sys)


#     def run_pipeline(self):
#         try:
#             feature_store_file_path = self.start_data_ingestion()
#             train_arr,test_arr = self.start_data_transformation(feature_store_file_path)
#             r2_square = self.start_model_trianing(train_arr,test_arr)

#             print('training completed, Training model score',r2_square)

#         except Exception as e:
#             raise CustomException(e,sys)



import sys
import os
import traceback
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Components.data_ingestion import DataIngestion
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer
from src.exception import CustomException

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            feature_store_file_path = data_ingestion.initiate_data_ingestion()
            if not os.path.exists(feature_store_file_path):
                raise FileNotFoundError(f"Feature store file path does not exist: {feature_store_file_path}")
            return feature_store_file_path
        except Exception as e:
            raise CustomException(f"Data ingestion failed: {e}", sys)

    def start_data_transformation(self, feature_store_file_path):
        try:
            data_transformation = DataTransformation(feature_store_file_path=feature_store_file_path)
            # Ensure method name and return values are correct
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation()
            return train_arr, test_arr, preprocessor_path
        except FileNotFoundError as fe:
            raise CustomException(f"File not found during data transformation: {fe}", sys)
        except Exception as e:
            raise CustomException(f"Unexpected error in data transformation: {e} | Traceback: {traceback.format_exc()}", sys)

    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            return model_score
        except Exception as e:
            raise CustomException(f"Model training failed: {e}", sys)

    def run_pipeline(self):
        try:
            feature_store_file_path = self.start_data_ingestion()
            train_arr, test_arr, preprocessor_path = self.start_data_transformation(feature_store_file_path)
            r2_square = self.start_model_training(train_arr, test_arr)

            print('Training completed successfully. Model score:', r2_square)

        except CustomException as ce:
            print(ce)
        except Exception as e:
            print(f"Unexpected error in pipeline: {e} | Traceback: {traceback.format_exc()}")
