from pyspark.sql import SparkSession
from pyspark.sql.types import StringType,StructType,StructField,IntegerType
spark=SparkSession.builder.appName('Filter Function').getOrCreate()
data=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\fruits.csv',header=True,inferSchema=True)
schema=StructType([
    StructField("Name",StringType),
    StructField("Count",IntegerType),
    StructField("Price",IntegerType)
])

