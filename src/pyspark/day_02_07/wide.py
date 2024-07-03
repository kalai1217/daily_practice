from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Create a SparkSession
spark = SparkSession.builder.appName("WideTransformationsExample").getOrCreate()

# Create sample DataFrames
dept_data = [
    (1, "Sales"),
    (2, "Marketing"),
    (3, "Engineering")
]
dept_columns = ["dept_id", "dept_name"]
dept_df = spark.createDataFrame(dept_data, dept_columns)

emp_data = [
    (1, "John", "Doe", 1, 80000.0),
    (2, "Jane", "Smith", 2, 65000.0),
    (3, "Michael", "Johnson", 3, 90000.0),
    (4, "Emily", "Williams", 1, 75000.0),
    (5, "David", "Brown", 2, 60000.0)
]
emp_columns = ["emp_id", "first_name", "last_name", "dept_id", "salary"]
emp_df = spark.createDataFrame(emp_data, emp_columns)

# Wide transformations
# Join
joined_df = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "inner")
joined_df.show()

# GroupBy and Aggregate
agg_df = emp_df.groupBy("dept_id").agg(
    expr("sum(salary) AS total_salary"),
    expr("avg(salary) AS avg_salary")
)
agg_df.show()

# Sort
sorted_df = emp_df.sort(col("salary").desc())
sorted_df.show()

# Union
new_emp_data = [
    (6, "Sarah", "Taylor", 3, 85000.0),
    (7, "Robert", "Miller", 1, 70000.0)
]
new_emp_df = spark.createDataFrame(new_emp_data, emp_columns)
union_df = emp_df.union(new_emp_df)
union_df.show()

input("Exit")