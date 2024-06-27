from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('custom').getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\exp.csv',header=True,inferSchema=True)
df_columns=df.columns
print(df_columns)
print(df.head(2))
df.select(['Age','Exp']).show()
#show the data types
print(df.dtypes)
print(df.describe())
#based on index the min and max of string works
print(df.describe().show())