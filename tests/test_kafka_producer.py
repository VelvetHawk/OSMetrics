import unittest


class TestKafkaProducer(unittest.TestCase):
	def test_get_cpu_metrics(self):
		print("Meep")
		self.assertEqual(True, True)

	def test_get_memory_metrics(self):
		self.assertEqual(True, True)


if __name__ == '__main__':
	unittest.main()
