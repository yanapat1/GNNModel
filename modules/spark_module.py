from pyspark.sql import SparkSession

def create_spark_session():
    spark = SparkSession.builder.master('foview').appName('gnn').getOrCreate()
    return spark