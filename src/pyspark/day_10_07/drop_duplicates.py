import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('sparkdf').getOrCreate()

data = [["1", "sravan", "company 1"], 
        ["2", "ojaswi", "company 1"], 
        ["3", "rohith", "company 2"],
        ["4", "sridevi", "company 1"], 
        ["1", "sravan", "company 1"], 
        ["4", "sridevi", "company 1"]]

columns = ['Employee ID', 'Employee NAME', 'Company']

dataframe = spark.createDataFrame(data, columns)

print('Actual data in dataframe')
dataframe.show()

print('Distinct data after dropping duplicate rows')
dataframe.distinct().show()

print('Distinct data in Employee ID and Employee NAME')
dataframe.select(['Employee ID', 'Employee NAME']).distinct().show()

print('Data after removing duplicates using dropDuplicates()')
dataframe.dropDuplicates().show()

print('Data after removing duplicates in Employee ID and Employee NAME using dropDuplicates()')
dataframe.select(['Employee ID', 'Employee NAME']).dropDuplicates().show()
