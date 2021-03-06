import os
import sys
import logging

# Set up environment variables
KAFKA_PRODUCER_ID = os.getenv("KAFKA_PRODUCER_ID")
KAFKA_CONSUMER_ID = os.getenv("KAFKA_CONSUMER_ID")
KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_PORT = os.getenv("KAFKA_PORT")
KAFKA_SSL_CA_FILE = os.getenv("KAFKA_SSL_CA_FILE")
KAFKA_SSL_CERT_FILE = os.getenv("KAFKA_SSL_CERT_FILE")
KAFKA_SSL_KEY_FILE = os.getenv("KAFKA_SSL_KEY_FILE")
KAFKA_TOPIC_NAME = os.getenv("KAFKA_TOPIC_NAME")

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB_NAME = os.getenv("PG_DB_NAME")
PG_DB_USER = os.getenv("PG_DB_USER")
PG_USER_PASSWORD = os.getenv("PG_USER_PASSWORD")
PG_SSL_CA_FILE = os.getenv("PG_SSL_CA_FILE")
PG_SERVICE_URI = "postgres://{}:{}@{}:{}/{}?sslmode=require".format(
	PG_DB_USER, PG_USER_PASSWORD, PG_HOST, PG_PORT, PG_DB_NAME
)


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Format Log messages
formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s]: %(message)s')

# Set up a handler to print to  the console
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)

# Set logger handler
logger.addHandler(handler)
