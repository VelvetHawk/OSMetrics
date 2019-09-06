# Code for psutil sourced from:
# https://pypi.org/project/psutil/

# Producer code sourced from:
# https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

import psutil
import kafka


class Producer:
	"""
	Creates a Kafka Producer for a Kafka Topic and sends messages to this
	topic about metrics from the current operating system.
	"""

	def __init__(self, host, port, ca_file, cert_file, key_file, kafka_topic):
		# Set up kafka producer
		self.producer = kafka.KafkaProducer(
			bootstrap_servers="{}:{}".format(host, port),
			security_protocol="SSL",
			ssl_cafile=ca_file,
			ssl_certfile=cert_file,
			ssl_keyfile=key_file,
		)
		self.kafka_topic = kafka_topic
		self.cpu_percentages = None
		self.memory_percentages = None

	def get_cpu_metrics(self):
		"""
		Gets the utilisation percentage and temperature for each CPU
		"""
		self.cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)

	def get_memory_metrics(self):
		"""
		Gets the utilisation percentage for both virtual memory and
		swap space on the target OS
		"""
		self.memory_percentages = [psutil.virtual_memory().percent, psutil.swap_memory().percent]

	def send_metrics(self):
		pass
