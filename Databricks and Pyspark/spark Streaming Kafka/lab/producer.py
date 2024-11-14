from kafka import KafkaProducer
import json
import time

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Use 'kafka' as the Kafka service name from Docker Compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate sending a few events to Kafka
for i in range(5):
    event = {'event_type': 'add_to_cart', 'product_id': str(i), 'user_id': f'user_{i}'}
    print(f"Sending event: {event}")
    producer.send('ecommerce-events', event)  # Sending the event to the Kafka topic
    time.sleep(1)

# Flush the producer to ensure all messages are sent
producer.flush()
print("All messages sent.")
