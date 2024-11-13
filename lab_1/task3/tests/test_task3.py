import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task3.src.task3 import insertion_sort_r


class TestInsertionSortReversed(unittest.TestCase):
    def test_should_sort_small_array(self):
        # given
        data = random.sample(range(10 ** 5), 10 ** 2)
        expected_result = sorted(data, reverse=True)

        # when
        result = insertion_sort_r(len(data), data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_large_array(self):
        # given
        data = random.sample(range(10 ** 9), 10 ** 5)
        expected_result = sorted(data, reverse=True)

        # when
        result = insertion_sort_r(len(data), data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
