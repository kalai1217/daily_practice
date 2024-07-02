# Databricks notebook source
data=[(1,'kalai','M',2000),(2,'sri','M',3000),(3,'viji','F',4000),(4,'jeeva','M',5000),(5,'bot','',0000)]
schema=['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import col
df.sort(col('id').desc()).show()

# COMMAND ----------

df.sort(col('id').desc(),col('name').asc()).show()

# COMMAND ----------

df.orderBy(col('id').desc(),col('name').asc()).show()
