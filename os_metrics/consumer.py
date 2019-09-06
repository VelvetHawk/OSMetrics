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
			security_protocol="SSL",
			ssl_cafile=ca_file,
			ssl_certfile=cert_file,
			ssl_keyfile=key_file,
		)
