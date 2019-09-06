#!/usr/bin/env python3

"""
This module uses a Kafka Producer to extract metrics from the current operating
system and send them to a Kafka Topic, where a Kafka Consumer then takes those
messages and logs them to a PostgreSQL database
"""

import platform
import time

import psutil

from os_metrics import producer
from os_metrics import consumer
import config


# Control for event loop task
stop_task = False

# Get basic OS information
os_name = platform.system()
os_release = platform.release()
os_architecture = "{} ({})".format(platform.architecture()[0], platform.machine())
os_version = platform.version()

# Get information about processor and memory
processor = platform.processor()
cpu_physical_cores = psutil.cpu_count(logical=False)
cpu_logical_cores = psutil.cpu_count(logical=True)
total_ram = psutil.virtual_memory().total
total_swap_space = psutil.swap_memory().total

# Create Kafka Producer and create connection to topic
producer = producer.Producer(
	host=config.KAFKA_HOST,
	port=config.KAFKA_PORT,
	ca_file=config.KAFKA_SSL_CA_FILE,
	cert_file=config.KAFKA_SSL_CERT_FILE,
	key_file=config.KAFKA_SSL_KEY_FILE,
	kafka_topic=config.KAFKA_TOPIC_NAME
)

# Create Kafka Consumer and create connection to topic
consumer = consumer.Consumer(
	host=config.KAFKA_HOST,
	port=config.KAFKA_PORT,
	ca_file=config.KAFKA_SSL_CA_FILE,
	cert_file=config.KAFKA_SSL_CERT_FILE,
	key_file=config.KAFKA_SSL_KEY_FILE,
	kafka_topic=config.KAFKA_TOPIC_NAME,
	service_uri=config.PG_SERVICE_URI
)

# Run for 10 seconds, with 1 second intervals
i = 0
while i < 10:
	# producer.send_metrics()
	consumer.consume()
	i += 1
	time.sleep(1)  # Sleep 1 second

# Close connections and stop producer/consumer
producer.stop()
consumer.stop()
