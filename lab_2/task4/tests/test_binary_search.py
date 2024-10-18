import unittest
from lab_2.task4.task4 import binary_search


class BinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(6, [1, 1, 3, 4, 5, 6], 3, [1, 2, 5]), [0, -1, 4])


