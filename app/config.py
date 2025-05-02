# Vars and Configurations
import os

# Root of project
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# path for raw_data
RAW_DATA_PATH = os.path.join(ROOT,'data','patient.csv')

# App_name for SparkSession
APP_NAME = 'fhir_pipeline'

# Sparks configs for SparkSession
SPARK_CONFIGS = {
    'spark.executor.heartbeatInterval' : '60s',
    'spark.network.timeout' : '600s'
}


