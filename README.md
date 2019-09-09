# OSMetrics
This is a Python package to extract operating
system metrics and then send them through an
Apache Kafka Producer to a Kafka Topic where
a Kafka Consumer will extract the data from the
topic and log it into a PostgreSQL database.

## Setup
To install the module locally (since it's not on PyPI), use:
```
python setup.py install
```

If you need to later install requirements manually, you 
can use:
```
pip install -r requirements.txt
```

Before you run the code, make sure to also set
the following environment variables in your
environment or your IDE:

For the Apache Kafka Producer and Consumer:

Name          | Value
:---: |:---:
KAFKA_PRODUCER_ID | Client ID for the Kafka Producer
KAFKA_CONSUMER_ID | Client ID for the Kafka Consumer
KAFKA_HOST | Address of the host for the Kafka server
KAFKA_PORT | Port number
KAFKA_SSL_CA_FILE | path/to/file 
KAFKA_SSL_CERT_FILE | path/to/file 
KAFKA_SSL_KEY_FILE | path/to/file 
KAFKA_SSL_CA_FILE | path/to/file 
KAFKA_TOPIC_NAME| Name of the topic

For the PostgreSQL Database:

Name        | Value
:---: |:---:
PG_HOST | Address of the host for the PostgreSQL server
PG_PORT | Port number
PG_DB_NAME | Database name
PG_DB_USER | Name of the user account
PG_USER_PASSWORD | User account password
PG_SSL_CA_FILE | path/to/file
  
## Running
You can then run the `os_metrics` module directly
by using:
```
python -m os_metrics
```
Currently set to run for ~10 seconds
before exiting.

## Testing
Discover and run all tests automatically:
```
python -m unittest discover
```
or specify the `tests` module directly:
```
python -m tests
```
All tests must be prefixed with a `test_`
prefix.

## Logging
Default logging level is `DEBUG` and the
default output stream is configured for
`stdout`.
