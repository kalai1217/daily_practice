# Databricks notebook source
data=[(1,'kalai',['python','adf']),(2,'sriram',['r','sql']),(3,'moni',[])]
schema=['id','name','skill']
df=spark.createDataFrame(data,schema)
df.show()
df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col,explode,explode_outer
df1=df.withColumn('skills',explode(col('skill')))
df1.show()
df2=df.withColumn('skills',explode_outer(col('skill')))
df2.show()



# COMMAND ----------

data=[(1,'kalai','kalai,arasan'),(2,'sri','sri,ram')]
schema=['id','name','full_name']
new_df=spark.createDataFrame(data,schema)
new_df.show()
new_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import split,col
new_df1=new_df.withColumn('full_name',split(col('full_name'),',').alias('newcol'))
new_df1.show()
new_df1.printSchema()

# COMMAND ----------

data=[(1,'kalai','python','adf'),(2,'sriram','r','sql')]
schema=['id','name','skill1','skill2']
df_array=spark.createDataFrame(data,schema)
df_array.show()
df_array.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col,array
df_array1=df_array.withColumn('skills',array(col('skill1'),col('skill2')))
df_array1.show()



# COMMAND ----------

from pyspark.sql.functions import col,array_contains
df_array2=df_array1.withColumn('haspython',array_contains(col('skills'),'python'))
df_array2.show()

# COMMAND ----------

# data=[(1,'kalai',['python','adf']),(2,'sriram',['r','sql']),(3,'moni',[])]
# schema=['id','name','skill']
# df=spark.createDataFrame(data,schema)
df.show()
df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col,posexplode
dfy=df.withColumn('pos_skills',posexplode(col('skill').alias('pos','skilltype')))
dfy.show()

# COMMAND ----------

df_exploded = df.withColumn("product", explode(col("products"))) \
                .withColumn("price", explode(col("price"))) \
                .select("order_id", col("product").alias("products"), "price")
