# OSMetrics
This is a Python package to extract operating
system metrics and then send them through an
Apache Kafka Producer to a Kafka Topic where
a Kafka Consumer will extract the data from the
topic and log it into a PostgreSQL database.

## Testing

### Command line testing
Discover and run all tests automatically:
```
python -m unittest discover
```
or specify the `tests` module directly:
```
python tests
```
All tests must be prefixed with a `test_` prefix.


