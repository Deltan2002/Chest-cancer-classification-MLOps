from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            logger.info("Starting model evaluation...")
            evaluation.evaluation()
            logger.info("Model evaluation completed. Saving scores...")
            evaluation.save_score()
            logger.info("Scores saved successfully.")
            # Optionally log into MLflow
            # logger.info("Logging evaluation into MLflow...")
            # evaluation.log_into_mlflow()
            # logger.info("Evaluation logged into MLflow successfully.")
        except Exception as e:
            logger.error(f"An error occurred during evaluation: {e}")
            raise