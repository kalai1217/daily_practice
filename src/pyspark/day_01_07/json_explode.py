# Databricks notebook source

from pyspark.sql.types import StructType, StructField, StringType



# Define the schema
schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("products", StringType(), True),
    StructField("price", StringType(), True)
])

# Create data
data = [
    {"order_id": "1234", "products": "prd1, prd2", "price": "pr1, pr2"},
    {"order_id": "1235", "products": "prd1, prd2, prd3", "price": "pr1, pr2, pr3"}
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()


# COMMAND ----------

from pyspark.sql.functions import split,col,explode,posexplode,arrays_zip
df1=df.withColumn('products',split(col('products'),','))
df1.show()

# COMMAND ----------

df2=df1.withColumn('price',split(col('price'),','))
df2.show()

# COMMAND ----------

from pyspark.sql.functions import arrays_zip
df3=df2.withColumn('zipped',arrays_zip('products','price'))
df3.show()

# COMMAND ----------

df_zipped = df2.withColumn("zipped", arrays_zip("products", "price"))
df_exploded = df_zipped.withColumn("exploded", explode("zipped")) 
df_exploded.show()

# COMMAND ----------

df_exploded.select("order_id", col("exploded.products").alias("products"), col("exploded.price").alias("price")).show()

# COMMAND ----------


