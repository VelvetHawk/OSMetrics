# Consumer code sourced from:
# https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

# PostegreSQL code sourced from:
# https://help.aiven.io/en/articles/489573-getting-started-with-aiven-postgresql

import kafka


class Consumer:
	"""
	Consumes messages posted to a Kafka Topic and stores them in the
	specified PostegreSQL database
	"""

	def __init__(self, host, port, ca_file, cert_file, key_file, kafka_topic,
			service_uri):
		self.consumer = kafka.KafkaConsumer(
			kafka_topic,
			auto_offset_reset="earliest",
			bootstrap_servers="{}:{}".format(host, port),
			group_id="python-test",
			security_protocol="SSL",
			ssl_cafile=ca_file,
			ssl_certfile=cert_file,
			ssl_keyfile=key_file,
		)

	def consume(self):
		"""
		Check the Kafka Topic for new messages and if present,
		send to the PostgreSQL database
		"""
		raw_messages = self.consumer.poll(timeout_ms=1000)
		for topic, messages in raw_messages.items():
			print("Topic: {}".format(topic))
			for message in messages:
				print("Message: {}".format(message))
		self.consumer.commit()

	def stop(self):
		self.consumer.close()
