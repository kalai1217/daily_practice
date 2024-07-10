from pyspark.sql.window import Window
import pyspark
 
# importing sparksession
from pyspark.sql import SparkSession
 
# creating a sparksession object
# and providing appName
spark = SparkSession.builder.appName("pyspark_window").getOrCreate()
 
# sample data for dataframe
sampleData = (("Ram", 28, "Sales", 3000),
              ("Meena", 33, "Sales", 4600),
              ("Robin", 40, "Sales", 4100),
              ("Kunal", 25, "Finance", 3000),
              ("Ram", 28, "Sales", 3000),
              ("Srishti", 46, "Management", 3300),
              ("Jeny", 26, "Finance", 3900),
              ("Hitesh", 30, "Marketing", 3000),
              ("Kailash", 29, "Marketing", 2000),
              ("Sharad", 39, "Sales", 4100)
              )
 
# column names for dataframe
columns = ["Employee_Name", "Age",
           "Department", "Salary"]
 
# creating the dataframe df
df = spark.createDataFrame(data=sampleData,
                           schema=columns)
 
# importing Window from pyspark.sql.window
 
# creating a window
# partition of dataframe
windowPartition = Window.partitionBy("Department").orderBy("Age")
 
# print schema
df.printSchema()
 
# show df
df.show()
 
# applying window function with
# the help of DataFrame.withColumn
df.withColumn("cume_dist",
              cume_dist().over(windowPartition)).show()

df.withColumn("Lag", lag("Salary", 2).over(windowPartition)) \
    .show()
df.withColumn("Lead", lead("salary", 2).over(windowPartition)) \
    .show()
sampleData = ((101, "Ram", "Biology", 80),
              (103, "Meena", "Social Science", 78),
              (104, "Robin", "Sanskrit", 58),
              (102, "Kunal", "Phisycs", 89),
              (101, "Ram", "Biology", 80),
              (106, "Srishti", "Maths", 70),
              (108, "Jeny", "Physics", 75),
              (107, "Hitesh", "Maths", 88),
              (109, "Kailash", "Maths", 90),
              (105, "Sharad", "Social Science", 84)
              )
 
# column names for dataframe
columns = ["Roll_No", "Student_Name", "Subject", "Marks"]
 
# creating the dataframe df
df2 = spark.createDataFrame(data=sampleData,
                            schema=columns)
 
# importing window from pyspark.sql.window
 
# creating a window partition of dataframe
windowPartition = Window.partitionBy("Subject").orderBy("Marks")
 
# print schema
df2.printSchema()
 
# show df
df2.show()
df2.withColumn("row_number", 
               row_number().over(windowPartition)).show()

df2.withColumn("rank", rank().over(windowPartition)) \
    .show()

df2.withColumn("dense_rank",
               dense_rank().over(windowPartition)).show()
