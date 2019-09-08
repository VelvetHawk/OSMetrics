# Consumer code sourced from:
# https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

# PostegreSQL code sourced from:
# https://help.aiven.io/en/articles/489573-getting-started-with-aiven-postgresql

import json

import kafka
from psycopg2.extras import RealDictCursor
import psycopg2

from config import logger


class Consumer:
	"""
	Consumes messages posted to a Kafka Topic and stores them in the
	specified PostegreSQL database
	"""

	def __init__(self, client_id, host, port, ca_file, cert_file, key_file, kafka_topic,
			service_uri):
		self.consumer = kafka.KafkaConsumer(
			kafka_topic,
			client_id=client_id,
			auto_offset_reset="earliest",
			bootstrap_servers="{}:{}".format(host, port),
			group_id="python-test",
			security_protocol="SSL",
			ssl_cafile=ca_file,
			ssl_certfile=cert_file,
			ssl_keyfile=key_file,
		)
		self.db_connection = psycopg2.connect(service_uri)
		self.cursor = self.db_connection.cursor(cursor_factory=RealDictCursor)

	def consume(self):
		"""
		Check the Kafka Topic for new messages and if present,
		send to the PostgreSQL database
		"""
		raw_messages = self.consumer.poll(timeout_ms=1000)
		for topic, messages in raw_messages.items():
			logger.debug("Topic: {}".format(topic))
			for message in messages:
				metrics = json.loads(message.value.decode('utf-8'))
				logger.debug("C Message: {}".format(metrics))
				# Check message types, case insensitive
				if metrics['type'].lower() == "log":
					# For each CPU core, add a separate entry to database
					i = 0
					for cpu in metrics['content']['cpu_metrics']:
						self.cursor.execute(
							"INSERT INTO cpu_metrics"
							"(producer_id, date_time, operating_system, core, load_percentage)"
							" values "
							"('{}', NOW() AT TIME ZONE 'UTC', '{}', {}, {});".format(
								metrics['content']['producer_id'],
								metrics['content']['mac_id'],
								i,
								cpu
							)
						)
						self.db_connection.commit()
						i += 1
					# Add memory metrics to database
					query = \
						"INSERT INTO memory_metrics" \
						"(producer_id, date_time, operating_system, ram_load_percentage," \
						"swap_load_percentage)" \
						" values " \
						"('{}', NOW() AT TIME ZONE 'UTC', '{}', {}, {});".format(
							metrics['content']['producer_id'],
							metrics['content']['mac_id'],
							metrics['content']['memory_metrics'][0],
							metrics['content']['memory_metrics'][1]
						)
					logger.debug("Query: {}".format(query))
					self.cursor.execute(query)
					self.db_connection.commit()
					# result = self.cursor.fetchone()
					# print("Result: {}".format(result))
				elif metrics['type'].lower() == "registration":
					self.cursor.execute("SELECT * FROM operating_systems WHERE "
										"id='{}'".format(metrics['content']['mac_id']))
					result = self.cursor.fetchone()
					logger.debug("OS Result: {}".format(result))
					if not result:
						query = \
							"INSERT INTO operating_systems" \
							"(id, name, release, architecture, version, processor, " \
							"physical_cores, logical_cores, total_ram, total_swapspace)" \
							"values" \
							"('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {});".format(
								metrics['content']['mac_id'],
								metrics['content']['os_name'],
								metrics['content']['os_release'],
								metrics['content']['os_architecture'],
								metrics['content']['os_version'],
								metrics['content']['processor'],
								metrics['content']['cpu_physical_cores'],
								metrics['content']['cpu_logical_cores'],
								metrics['content']['total_ram'],
								metrics['content']['total_swap_space'],
							)
						logger.debug("Query: {}".format(query))
						self.cursor.execute(query)
						self.db_connection.commit()
						# result = self.cursor.fetchone()
						# print("Result: {}".format(result))
		# Flush any lingering messages
		self.consumer.commit()

	def stop(self):
		self.consumer.close()
