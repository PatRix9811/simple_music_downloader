import main
import unittest

class SimpleTest(unittest.TestCase):
	def test_load_list(self):
		result = main.load_title_list()
		self.assertIsInstance(result, list)

	def test_find_track1(self):
		result = main.find_track('Chada, Bezczel, ZBUKU ft. KaeN - Kontrabanda: To nie nasz klimat')
		self.assertIsInstance(result, str)

	def test_find_track2(self):
		result = main.find_track('dsfgsdfghfdsgsdfhasdg')
		self.assertEqual(result, None)

if __name__ == '__main__':
	unittest.main()