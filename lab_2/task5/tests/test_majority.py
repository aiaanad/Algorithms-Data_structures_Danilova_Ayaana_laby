import unittest
from lab_2.task5.src.task5 import majority


class Majority(unittest.TestCase):
    def test_majority(self):
        self.assertEqual(majority(6, [1, 3, 6, 1, 8, 1]), 0)
        self.assertEqual(majority(6, [1, 3, 1, 1, 8, 1]), 1)

