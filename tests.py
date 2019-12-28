import main
import unittest

class SimpleTest(unittest.TestCase):
	def test_one(self):
		result = main.load_title_list()
		self.assertIsInstance(result, list)


if __name__ == '__main__':
	unittest.main()