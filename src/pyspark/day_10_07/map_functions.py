from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName().getOrCreate()

data = [
    (1, ["apple", "banana", "cherry"]),
    (2, ["orange", "kiwi"]),
    (3, ["grape", "watermelon", "mango"])
]

df = spark.createDataFrame(data, ["id", "fruits"])
df.show()

df.select(col("fruits"), explode(col("fruits")).alias("fruit")).show()

data2 = [
    (1, [1, 2, 3]),
    (2, [4, 5, 6]),
    (3, [7, 8, 9])
]

df2 = spark.createDataFrame(data2, ["id", "numbers"])
df2.show()

df2.select(col("numbers"), array_contains(col("numbers"), 2).alias("contains_2")).show()

df2.select(col("numbers"), arrays_zip(col("numbers"), array(10, 20, 30)).alias("zipped_arrays")).show()

df2.select(col("numbers"), size(col("numbers")).alias("size")).show()

df2.select(col("numbers"), sort_array(col("numbers")).alias("sorted")).show()

df2.select(col("numbers"), reverse(col("numbers")).alias("reversed")).show()

df2.select(col("numbers"), array_distinct(col("numbers")).alias("distinct")).show()

df2.select(col("numbers"), array_intersect(col("numbers"), array(1, 3, 5, 7)).alias("intersect")).show()

df2.select(col("numbers"), array_union(col("numbers"), array(1, 3, 5, 7)).alias("union")).show()

df2.select(col("numbers"), array_except(col("numbers"), array(1, 3, 5, 7)).alias("except")).show()

data3 = [
    (1, [1, 2, 3], [4, 5, 6]),
    (2, [4, 5, 6], [1, 2, 3]),
    (3, [7, 8, 9], [9, 8, 7])
]

df3 = spark.createDataFrame(data3, ["id", "numbers1", "numbers2"])
df3.show()

df3.select(col("numbers1"), col("numbers2"), arrays_overlap(col("numbers1"), col("numbers2")).alias("overlap")).show()

data4 = [
    (1, [10, 20, 30]),
    (2, [40, 50, 60]),
    (3, [70, 80, 90])
]

df4 = spark.createDataFrame(data4, ["id", "numbers"])
df4.show()

df4.select(col("numbers"), array_max(col("numbers")).alias("max")).show()

df4.select(col("numbers"), array_min(col("numbers")).alias("min")).show()
