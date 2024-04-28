from Text_summary.logging import logger
from Text_summary.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline

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