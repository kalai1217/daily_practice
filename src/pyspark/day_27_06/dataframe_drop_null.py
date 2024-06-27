from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Write DataFrame to CSV").getOrCreate()
# Create a DataFrame with the provided data
data = [("Kalai", 22, 3), ("Sri",None , 2), ("Viji", 35, 10), ("Jeeva", 40, None),(None,None,None)]
columns = ["Name", "Age", "Exp"]
df = spark.createDataFrame(data, columns)
df.show()
#drop null values how="any"
df.na.drop().show()
#drop null values
df.na.drop(how='all').show()
#threshold value atleast number of non-null values shouldbe present
df.na.drop(how='any',thresh=2).show()
#subset drop values only from a sepcific column
df.na.drop(how='any',subset=['Exp']).show()