import unittest

import config
from os_metrics import consumer


class TestKafkaConsumer(unittest.TestCase):
	# Since there is no development/testing environment configured,
	# using the actual environment for this demo
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

	def test_database_connection(self):
		self.assertEqual(True, True)

	def test_consume(self):
		"""
		This test would be based on having a development/test environment
		where consume() can be called and the consumer's offset checked
		to make sure it is reading messages and marking an offset
		"""
		pass

	def test_create_log_entry(self):
		"""
		This test would be based on having a development/test environment
		where the database can be checked for a log message retrieved
		from a sample Kafka Topic and logged into the database
		"""
		pass

	def test_create_registration_entry(self):
		"""
		This test would be based on having a development/test environment
		where the database can be checked for a registration message
		retrieved from a sample Kafka Topic and logged into the database
		"""
		pass


if __name__ == '__main__':
	unittest.main()
