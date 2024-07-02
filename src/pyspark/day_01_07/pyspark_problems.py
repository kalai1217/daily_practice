# Databricks notebook source
# MAGIC %md
# MAGIC ##find the latest order status
# MAGIC

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

from pyspark.sql.functions import rank,col
from pyspark.sql.window import Window
window=Window.partitionBy('order_no').orderBy(col('timestamp').desc())
df1=df.withColumn('rank',rank().over(window))

# COMMAND ----------

df1.show()

# COMMAND ----------

df1.filter(col('rank')==1).show()
