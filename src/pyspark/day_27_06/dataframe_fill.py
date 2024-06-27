from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('custom').getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\fruits.csv',header=True,inferSchema=True)
new_df=df.na.fill(0,['Count'])