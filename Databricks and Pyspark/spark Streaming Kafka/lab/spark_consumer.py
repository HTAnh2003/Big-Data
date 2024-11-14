from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("EcommerceEvents") \
    .master("local[*]") \
    .getOrCreate()

# Read from Kafka topic
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "ecommerce-events") \
    .load()

# Define schema for the Kafka data
schema = StructType([
    StructField("event_type", StringType()),
    StructField("product_id", StringType()),
    StructField("user_id", StringType())
])

# Parse the data as JSON
events_df = df.selectExpr("CAST(value AS STRING)") \
              .select(from_json(col("value"), schema).alias("data")) \
              .select("data.*")

# Write to console for demo purposes
query = events_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Await termination of the stream
query.awaitTermination()
