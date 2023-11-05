from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split


if __name__ == "__main__":
    # Initialize a Spark session
    spark = SparkSession.builder.appName("week10PySpark").getOrCreate()

    # Load the dataset
    input_data = spark.read.csv("./nba.csv", header=True, inferSchema=True)

    # Data transformation example: Replace missing salary values with 0
    input_data = input_data.na.fill({"Salary": 0})

    # calculate the average age of players by team
    input_data.createOrReplaceTempView("nba_players")

    result = spark.sql(
        "SELECT Team, AVG(Age) as avg_age FROM nba_players GROUP BY Team"
    )
    result.show()

    # Perform the data transformation
    # Extract the player's first name from the "Name" column:
    processed_data = input_data.withColumn("First_Name", split(col("Name"), " ")[0])

    # Show the transformed DataFrame
    processed_data.show()

    # Stop the SparkSession
    spark.stop()
