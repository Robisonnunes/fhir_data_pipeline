from pipeline.extraction import build_spark_session, spark_extract_csv
from config import *

def main():
    SparkSession = build_spark_session(APP_NAME, SPARK_CONFIGS)
    spark_extract_csv(SparkSession, RAW_DATA_PATH )

if __name__ == "__main__":
    main()
