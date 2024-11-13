import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task2.src.task2 import insertion_sort_plus


class TestInsertionSortPlus(unittest.TestCase):
    def test_should_sort_plus(self):
        # given
        data = 10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_result = [1, 2, 2, 2, 3, 5, 5, 6, 9, 1]

        # when
        result = insertion_sort_plus(len(data), data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
