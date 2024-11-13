import random
import time
import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task4.src.task4 import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_should_binary_search(self):
        # given
        data = 5, [1, 5, 8, 12, 13], 5, [8, 1, 23, 1, 11]
        expected_result = [2, 0, -1, 0, -1]

        # when
        result = binary_search(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
