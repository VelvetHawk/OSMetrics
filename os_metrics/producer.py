# Code for psutil sourced from:
# https://pypi.org/project/psutil/

# Producer code sourced from:
# https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

# MAC address code sourced from:
# https://www.geeksforgeeks.org/extracting-mac-address-using-python/

import platform
import json
import uuid
import re

import psutil
import kafka

from config import logger


class Producer:
	"""
	Creates a Kafka Producer for a Kafka Topic and sends messages to this
	topic about metrics from the current operating system.
	"""

	def __init__(self, client_id, host, port, ca_file, cert_file, key_file, kafka_topic):
		# Set up kafka producer
		self.producer = kafka.KafkaProducer(
			bootstrap_servers="{}:{}".format(host, port),
			client_id=client_id,
			security_protocol="SSL",
			ssl_cafile=ca_file,
			ssl_certfile=cert_file,
			ssl_keyfile=key_file,
		)
		self.client_id = client_id
		self.kafka_topic = kafka_topic
		self.cpu_percentages = None
		self.memory_percentages = None

		# Get basic OS information
		self.mac_id = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		self.os_name = platform.system()
		self.os_release = platform.release()
		self.os_architecture = "{} ({})".format(platform.architecture()[0], platform.machine())
		self.os_version = platform.version()

		# Get information about processor and memory
		self.processor = platform.processor()
		self.cpu_physical_cores = psutil.cpu_count(logical=False)
		self.cpu_logical_cores = psutil.cpu_count(logical=True)
		self.total_ram = psutil.virtual_memory().total
		self.total_swap_space = psutil.swap_memory().total

	def get_cpu_metrics(self) -> None:
		"""
		Gets the utilisation percentage and temperature for each CPU
		"""
		self.cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)

	def get_memory_metrics(self) -> None:
		"""
		Gets the utilisation percentage for both virtual memory and
		swap space on the target OS
		"""
		self.memory_percentages = [psutil.virtual_memory().percent, psutil.swap_memory().percent]

	def register_machine(self) -> None:
		"""
		Sends a message to the Kafka topic about the current machine. Uses the
		'registration' type to let the consumer know that this is a new entry
		"""
		message = {
			'type': 'registration',
			'content': {
				'mac_id': self.mac_id,
				'producer_id': self.client_id,
				'os_name': self.os_name,
				'os_release': self.os_release,
				'os_architecture': self.os_architecture,
				'os_version': self.os_version,
				'processor': self.processor,
				'cpu_physical_cores': self.cpu_physical_cores,
				'cpu_logical_cores': self.cpu_logical_cores,
				'total_ram': self.total_ram,
				'total_swap_space': self.total_swap_space
			}
		}
		logger.debug("Sending message: {}".format(message))
		self.producer.send(self.kafka_topic, json.dumps(message).encode("utf-8"))
		self.producer.flush()

	def send_metrics(self) -> None:
		"""
		Collect metrics and send them to the given Kafka Topic. Uses
		'log' type to send log messages.
		"""
		self.get_cpu_metrics()
		self.get_memory_metrics()
		message = {
			'type': 'log',
			'content': {
				'mac_id': self.mac_id,
				'producer_id': self.client_id,
				'cpu_metrics': self.cpu_percentages,
				'memory_metrics': self.memory_percentages
			}
		}
		self.producer.send(self.kafka_topic, json.dumps(message).encode("utf-8"))
		self.producer.flush()

	def stop(self) -> None:
		"""
		Close producer connection and cleanup
		"""
		self.producer.close(timeout=None)
