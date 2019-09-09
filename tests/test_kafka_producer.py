import unittest

import config
from os_metrics.producer import Producer


class TestKafkaProducer(unittest.TestCase):
	# Since there is no development/testing environment configured,
	# using the actual environment for this demo
	producer = Producer(
		client_id=config.KAFKA_PRODUCER_ID,
		host=config.KAFKA_HOST,
		port=config.KAFKA_PORT,
		ca_file=config.KAFKA_SSL_CA_FILE,
		cert_file=config.KAFKA_SSL_CERT_FILE,
		key_file=config.KAFKA_SSL_KEY_FILE,
		kafka_topic=config.KAFKA_TOPIC_NAME
	)

	def test_get_cpu_metrics(self):
		"""
		Check to make sure cpu_percentages is a list containing
		float values per CPU
		"""
		self.producer.get_cpu_metrics()
		# cpu_percentages is a list
		self.assertEquals(type(self.producer.cpu_percentages), list)
		# Each entry is a float
		for entry in self.producer.cpu_percentages:
			self.assertEquals(type(entry), float)

	def test_get_memory_metrics(self):
		"""
		Check to make sure memory_percentages contains 2 values,
		both floats
		"""
		self.producer.get_memory_metrics()
		# memory_percentages is a list of size 2
		self.assertEquals(type(self.producer.memory_percentages), list)
		self.assertEquals(len(self.producer.memory_percentages), 2)
		# Each entry is a float
		for entry in self.producer.memory_percentages:
			self.assertEquals(type(entry), float)

	def test_register_machine(self):
		"""
		This test would be based on having a development/test environment
		where register_machine() can be called and the Kafka Topic can then
		be checked for the registration message being sent
		"""
		pass

	def test_send_metrics(self):
		"""
		This test would be based on having a development/test environment
		where send_metrics() can be called and the Kafka Topic can then
		be checked for the log message being sent
		"""
		pass


if __name__ == '__main__':
	unittest.main()
