from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Create a SparkSession
spark = SparkSession.builder.appName("NarrowTransformationsExample").getOrCreate()

# Create a sample DataFrame
data = [
    (1, "John", "Doe", 35, 80000.0),
    (2, "Jane", "Smith", 28, 65000.0),
    (3, "Michael", "Johnson", 42, 90000.0),
    (4, "Emily", "Williams", 31, 75000.0),
    (5, "David", "Brown", 27, 60000.0)
]
columns = ["id", "first_name", "last_name", "age", "salary"]
df = spark.createDataFrame(data, columns)

# Narrow transformations
# Filter
filtered_df = df.filter((col("age") > 30) & (col("salary") > 70000.0))
filtered_df.show()

# Select
selected_df = df.select(col("first_name"), col("last_name"), expr("salary * 0.1 AS bonus"))
selected_df.show()

# Drop
dropped_df = df.drop("age")
dropped_df.show()

# Distinct
distinct_df = df.distinct()
distinct_df.show()

# Where
where_df = df.where(col("age") < 30)
where_df.show()

input("Exit")