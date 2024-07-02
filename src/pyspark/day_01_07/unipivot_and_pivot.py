# Databricks notebook source
from pyspark.sql.functions import expr
data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
      ("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
      ("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
      ("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]

columns= ["Product","Amount","Country"]
df = spark.createDataFrame(data = data, schema = columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col
df1=df.groupBy('Product').pivot('Country').sum('Amount')

# COMMAND ----------

df1.show()

# COMMAND ----------

from pyspark.sql.functions import expr
unpivotexpr="stack(4,'Canada',Canada,'China',China,'Mexcio',Mexico,'USA',usa) as (Country,Total)"
df2=df1.select('Product',expr(unpivotexpr)).where('Total is not null')
df2.show()

# COMMAND ----------


