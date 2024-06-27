from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Read csv in Data frame").getOrCreate()
df=spark.read.option('header','true').csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\exp.csv')
#Display only the first 3 records
df.show(3)
#selecting name column only
df.select('Name').show()