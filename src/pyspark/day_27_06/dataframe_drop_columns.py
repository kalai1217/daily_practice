from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('custom').getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\exp.csv',header=True,inferSchema=True)
print("Before drop")
df.show()
print("After drop")
df=df.drop('Age')
df.show()