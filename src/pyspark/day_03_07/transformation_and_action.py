from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("DAG Example").getOrCreate()

# Sample Data (replace with your actual data source)
data = [
    (1, 1, "2024-01-05", 1000),
    (2, 2, "2024-01-10", 1500),
    (3, 3, "2024-02-15", 1200),
    (4, 1, "2024-02-20", 1800),
    (5, 2, "2024-03-05", 2000),
    (6, 3, "2024-03-10", 1600)
]

df = spark.createDataFrame(data, ["order_id", "customer_id", "order_date", "order_total"])

# Stage 1: Filter orders by year (simulates a separate task)
def filter_by_year(df, year):
  return df.where(df.order_date.substr(1, 4) == year)

# Stage 2: Calculate monthly revenue (simulates a separate task)
def calculate_monthly_revenue(df):
  return df.groupBy("order_date").substr(df.order_date, 6, 2).agg(total_revenue=f"sum(order_total)")

# Simulate DAG execution (action triggers actual computations)
filtered_df_2024 = filter_by_year(df.copy(), "2024")  # Stage 1 (on a copy)
monthly_revenue_2024 = calculate_monthly_revenue(filtered_df_2024)  # Stage 2

# View results (triggers actual execution)
monthly_revenue_2024.show()

# Stop SparkSession
spark.stop()
