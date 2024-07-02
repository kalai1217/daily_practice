# Databricks notebook source
data=[(1,'kalai','M',2000),(2,'sri','M',3000),(3,'viji','F',4000),(4,'jeeva','M',5000),(5,'bot','',0000)]
schema=['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

from pyspark.sql.functions import col,when
df.select('name',
          when(col('gender')=='M','Male')
          .when(col('gender')=='F','Female')
          .otherwise('NA').alias('gender')).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ##alias asc desc cast and like functions
# MAGIC

# COMMAND ----------

df1=df.select(col('id').alias('emp_id'))
df1.show()

# COMMAND ----------

df.sort(col('salary').desc()).show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.select('id',col('salary').cast('int')).show()

# COMMAND ----------

df.filter(col('name').like('s%')).show()
