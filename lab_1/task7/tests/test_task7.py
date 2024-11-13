import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task7.src.task7 import sortland


class TestSortLand(unittest.TestCase):
    def test_should_sort_land(self):
        # given
        data = 5, [10.00, 8.70, 0.01, 5.00, 3.00]
        expected_result = (3, 4, 1)

        # when
        result = sortland(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
