# Databricks notebook source
data1=[(1,'kalai','M',2000),(2,'sri','M',3000)]
schema1=['id','name','gender','salary']
df1=spark.createDataFrame(data1,schema1)
data2=[(3,'viji','F',4000),(4,'jeeva','M',5000),(1,'kalai','M',2000)]
schema2=['id','name','gender','salary']
df2=spark.createDataFrame(data2,schema2)

df1.show()
df2.show()

df3=df1.union(df2)
df3.show()

# COMMAND ----------

df3=df1.unionAll(df2)
df3.show()

# COMMAND ----------


