from pyspark.sql import SparkSession
from pyspark.sql.types import *
spark=SparkSession.builder.appName("multiline").getOrCreate()
multiline_dataframe=spark.read.option("multiline","true").json(r"C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\multiline-zipcode.json")
multi_schmea=StructType([
  StructField("RecordNumber",IntegerType(),True),
  StructField("Zipcode",IntegerType(),True),
  StructField("ZipCodeType",StringType(),True),
  StructField("City",StringType(),True),
  StructField("State",StringType(),True)
])
dataframe_with_schema=spark.read.schema(multi_schmea).json(r"C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\multiline-zipcode.json")
# multiline_dataframe.printSchema()
# multiline_dataframe.show()
dataframe_with_schema.printSchema()
dataframe_with_schema.show()
