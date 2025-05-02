import os.path
from pyspark.sql import SparkSession, functions as F, Window, DataFrame
from pyspark.sql.types import *
import os


def build_spark_session(app_name: str, configs: dict) -> SparkSession:
    """
    Initializes a SparkSession

    Args:
        app_name (str) : The name of spark application

    Returns: SparkSession
    """
    try:
        # Creating SparkSession with necessary configurations
        spark_builder = SparkSession.builder.appName(app_name)

        # Configs
        for key, value in configs.items():
            spark_builder = spark_builder.config(key, value)

        # Crate Session Spark
        spark = spark_builder.getOrCreate()
        return spark

    except Exception as e:
        raise RuntimeError(f"Failed to initialize SparkSession: {e}")


def spark_extract_csv(SparkSession, path: str) -> DataFrame:
    """
    Extract data from source

    Args: path:Path from data source, SparkSession:SparkSession Created

    Return: Dataframe
    """

    try:
        spark = SparkSession
        df = spark.read.csv(path, header=True, inferSchema=True)
        df.show(5)
    except Exception as e:
        raise RecursionError(f"Failed to read data source")
