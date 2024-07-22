from Text_summary.logging import logger
from Text_summary.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_summary.pipelines.stage_02_dataValidation import DataValidationTrainingPipeline
from Text_summary.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_summary.pipelines.stage_04_Model_trainer import ModelTrainingPipeline

Stage_name = 'stage_01_data_ingestion'
try:
    logger.info(f"-----------------{Stage_name} Started----------------")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f"-----------------{Stage_name} Completed----------------")
except Exception as e:
    logger.error(f"-----------------{Stage_name} Failed----------------")
    logger.error(e)
    raise e

Stage_name = 'Stage_02_data_validation'
try:
    logger.info(f"-----------------{Stage_name} Started----------------")
    datavalidation = DataValidationTrainingPipeline()
    datavalidation.main()
    logger.info(f"-----------------{Stage_name} Completed----------------")
except Exception as e:
    logger.error(f"-----------------{Stage_name} Failed----------------")
    logger.error(e)
    raise e


Stage_name = 'Stage_03_data_transformation'
try:
    logger.info(f"-----------------{Stage_name} Started----------------")
    datatransformation = DataTransformationTrainingPipeline()
    datatransformation.main()
    logger.info(f"-----------------{Stage_name} Completed----------------")
except Exception as e:
    logger.error(f"-----------------{Stage_name} Failed----------------")
    logger.error(e)
    raise e

# Stage_name = 'Stage_04_model_training'
# try:
#     logger.info(f"-----------------{Stage_name} Started----------------")
#     modeltrainer = ModelTrainingPipeline()
#     modeltrainer.main()
#     logger.info(f"-----------------{Stage_name} Completed----------------")
# except Exception as e:
#     logger.error(f"-----------------{Stage_name} Failed----------------")
#     logger.error(e)
#     raise e