import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task5.src.task5 import majority


class TestMajority(unittest.TestCase):
    def test_should_majority(self):
        # given
        data = 6, [1, 3, 6, 1, 8, 1]
        expected_result = 0

        # when
        result = majority(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
