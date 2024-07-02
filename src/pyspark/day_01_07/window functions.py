# Databricks notebook source
data=[(1,'kalai','M',2000,1),(2,'sri','M',3000,1),(3,'viji','F',4000,2),(4,'jeeva','M',5000,2),(5,'bot','',0000,3)]
schema=['id','name','gender','salary','dept']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import max,count
df1=df.groupBy('dept').pivot('gender').agg(max('salary'))
df1.show()

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType
schema = StructType([
    StructField("name", StringType(), True),
    StructField("dept", StringType(), True),
    StructField("salary", IntegerType(), True)
])

# Sample data
data = [("John", "HR", 5000),
        ("Mike", "IT", 6000),
        ("Sara", "Finance", 7000),
        ("Smith", "Marketing", 8000),
        ("Rose", "Sales", 9000),
        ("Amy", "HR", 5500),
        ("Brian", "IT", 6500),
        ("Eva", "Finance", 7500),
        ("Adam", "Marketing", 8500),
        ("Ella", "Sales", 9500)]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()

# COMMAND ----------

from pyspark.sql.functions import row_number,rank,dense_rank,col
from pyspark.sql.window import Window
window=Window.partitionBy('dept').orderBy(col('salary').desc())
df1=df.withColumn('row_number',row_number().over(window))

# COMMAND ----------

df1.show()

# COMMAND ----------

df1.filter(col('row_number')==2).show()

# COMMAND ----------

df2=df1.withColumn('rank',rank().over(window))

# COMMAND ----------

df3=df2.withColumn('Dense_rank',dense_rank().over(window))

# COMMAND ----------

df3.show()

# COMMAND ----------

df3.filter((col('row_number')==2) | (col('rank')==2) | (col('Dense_rank')==2)).show()

# COMMAND ----------

from pyspark.sql.functions import col

df3.filter((col('row_number') == 2) | (col('rank') == 2) | (col('Dense_rank') == 2)).show()


# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType
from pyspark.sql.functions import to_timestamp


# Define the schema for the DataFrame
schema = StructType([
    StructField("order_no", IntegerType(), True),
    StructField("order_status", StringType(), True),
    StructField("timestamp", StringType(), True)  # Use StringType to parse the timestamp later
])

# Data for the DataFrame
data = [
    (1234, "placed", "30-06-2023 11:00 AM"),
    (1234, "being packed", "30-06-2023 05:00 PM"),
    (1234, "delivered", "01-07-2023 05:00 PM"),
    (1235, "placed", "30-07-2023 11:00 AM"),
    (1235, "being packed", "30-07-2023 05:00 PM")
]

# Create the DataFrame
df = spark.createDataFrame(data, schema)

# Convert the 'timestamp' column to actual timestamp type
df = df.withColumn("timestamp", to_timestamp("timestamp", "dd-MM-yyyy hh:mm a"))

# Show the DataFrame
df.show()


# COMMAND ----------

from pyspark.sql.functions import rank
from pyspark.sql.window import Window
window=Window.partitionBy('order_no').orderBy('timestamp')
df1=df.withColumn('rank',rank().over(window))

# COMMAND ----------

df1.show()

# COMMAND ----------


