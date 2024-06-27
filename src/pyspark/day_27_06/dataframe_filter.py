from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Filter Function').getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\fruits.csv',header=True,inferSchema=True)
df_filter=df.filter("Count>=11").select(['Name']).show()
df_filter=df.filter((df['Count']>11)|(df['Price']>78)).show()
