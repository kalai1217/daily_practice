# Databricks notebook source
data=[(1,'kalai','M',2000),(2,'sri','M',3000),(3,'viji','F',4000),(4,'jeeva','M',5000),(5,'bot','',0000)]
schema=['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import col
df.filter(col('salary')>3000).show()

# COMMAND ----------

df.filter((col('gender')=='F')&(col('salary')>2000)).show()

# COMMAND ----------

df.where((col('gender')=='F')&(col('salary')>2000)).show()

# COMMAND ----------

data=[(1,'kalai','M',2000),(2,'sri','M',3000),(3,'viji','F',4000),(4,'jeeva','M',5000),(5,'bot','',0000),(1,'kalai','M',2000)]
schema=['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

df.distinct().count()

# COMMAND ----------

df.dropDuplicates().show()

# COMMAND ----------

from pyspark.sql.functions import col
df.dropDuplicates(['gender']).show()
