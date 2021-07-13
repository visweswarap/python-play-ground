from pyspark import SparkContext
from pyspark.sql import SparkSession


def read_from_s3():
    csv_files = ["s3://platts-pdp-energy-transition-datasets-dev-s3-input/alternate_transportation_evs_annual-12-10-2020-100764646.csv"]
    sc = SparkContext()
    spark = SparkSession.builder.appName("python_play_ground").getOrCreate()
    data_df = spark.read.option("header", "true").csv(csv_files)
    print("download_csv_data end.")
    data_df.show()


read_from_s3()
