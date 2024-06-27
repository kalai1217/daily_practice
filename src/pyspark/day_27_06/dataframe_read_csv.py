from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Read csv in Data frame").getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\exp.csv')
df.printSchema()
df.show()