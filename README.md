# OSMetrics
This is a Python package to extract operating
system metrics and then send them through an
Apache Kafka Producer to a Kafka Topic where
a Kafka Consumer will extract the data from the
topic and log it into a PostgreSQL database.

## Running
Before you run the code, make sure to set the
following environment variables in your
environment or your IDE:

For the Apache Kafka Producer and Consumer:

Name          | Value
:---: |:---:
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
  

You can then run the `os_metrics` module directly
by using:
```
python -m os_metrics
```
It will continue to run indefinitely until a
keyboard interrupt is issued.

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
