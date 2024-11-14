FROM python:3.9-slim

# Install required libraries
RUN pip install kafka-python pyspark

# Set work directory and copy the scripts
WORKDIR /app
COPY producer.py spark_consumer.py /app/

# Use CMD to run the producer by default
CMD ["python", "producer.py"]
