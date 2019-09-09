#!/usr/bin/env python3

"""
This module uses a Kafka Producer to extract metrics from the current operating
system and send them to a Kafka Topic, where a Kafka Consumer then takes those
messages and logs them to a PostgreSQL database
"""

import time

from os_metrics import producer
from os_metrics import consumer
import config


# Control for event loop task
stop_task = False

# Create Kafka Producer and create connection to topic
producer = producer.Producer(
	client_id=config.KAFKA_PRODUCER_ID,
	host=config.KAFKA_HOST,
	port=config.KAFKA_PORT,
	ca_file=config.KAFKA_SSL_CA_FILE,
	cert_file=config.KAFKA_SSL_CERT_FILE,
	key_file=config.KAFKA_SSL_KEY_FILE,
	kafka_topic=config.KAFKA_TOPIC_NAME
)

# Create Kafka Consumer and create connection to topic
consumer = consumer.Consumer(
	client_id=config.KAFKA_CONSUMER_ID,
	host=config.KAFKA_HOST,
	port=config.KAFKA_PORT,
	ca_file=config.KAFKA_SSL_CA_FILE,
	cert_file=config.KAFKA_SSL_CERT_FILE,
	key_file=config.KAFKA_SSL_KEY_FILE,
	kafka_topic=config.KAFKA_TOPIC_NAME,
	service_uri=config.PG_SERVICE_URI
)

# Register machine details in Kafka Topic
producer.register_machine()
# Transfer details into database
consumer.consume()

# Run for 10 seconds, with 1 second intervals
for _ in range(10):
	producer.send_metrics()
	consumer.consume()
	time.sleep(1)  # Sleep 1 second

# Close connections and stop producer/consumer
producer.stop()
consumer.stop()
