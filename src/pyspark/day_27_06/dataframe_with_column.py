from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('custom').getOrCreate()
df=spark.read.csv(r'C:\Users\KalaiArasanJ\Desktop\pyspark_practice\resources\exp.csv',header=True,inferSchema=True)
#withColumn is used add a new column
df=df.withColumn('Exp after 2 years',df['Exp']+2)
df.show()
#drop the column
df=df.drop('Exp after 2 years')
df.show()
#rename with column
df=df.withColumnRenamed('Exp','Experience')
df.show()
