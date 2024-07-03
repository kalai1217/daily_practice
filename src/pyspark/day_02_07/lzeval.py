from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("LazyEvaluationExample").getOrCreate()

# Create a sample DataFrame
data = [
    (1, "John", "Doe", 35),
    (2, "Jane", "Smith", 28),
    (3, "Michael", "Johnson", 42),
    (4, "Emily", "Williams", 31),
    (5, "David", "Brown", 27)
]
columns = ["id", "first_name", "last_name", "age"]
df = spark.createDataFrame(data, columns)

# Transformations (Lazy Evaluation)
filtered_df = df.filter(df.age > 30)
selected_df = filtered_df.select("first_name", "last_name")
mapped_df = selected_df.rdd.map(lambda row: (row.first_name, row.last_name.upper()))

# No computation has happened yet

# Action (Triggers Evaluation)

result = mapped_df.collect()
print("Result:")
print(result)

input("Exit")