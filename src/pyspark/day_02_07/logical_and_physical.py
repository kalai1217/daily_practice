from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("DAGExample").getOrCreate()

# Create some sample data
data = [("John", 35, 60000), ("Mary", 28, 45000), ("Peter", 42, 80000)]
columns = ["name", "age", "salary"]
df = spark.createDataFrame(data, columns)

# Perform some transformations
df1 = df.filter("age > 30")
df2 = df1.select("name", "salary")
df3 = df2.withColumn("bonus", df2.salary * 0.1)
df4 = df3.drop("salary")

# Show the DAG and lineage
df4.explain(True)
input("Stop")