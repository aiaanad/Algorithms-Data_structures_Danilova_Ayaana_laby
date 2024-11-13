import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_3.task8.src.task8 import nearest_point


class TestNearestPoint(unittest.TestCase):
    def test_should_nearest_point_args1(self):
        # given
        data = 2, 1, [[1, 3], [-2, 2]]
        expected_result = [[-2, 2]]

        # when
        result = nearest_point(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_nearest_point_args2(self):
        # given
        data = 3, 2, [[3, 3], [5, -1], [-2, 4]]
        expected_result = [[3, 3], [-2, 4]]

        # when
        result = nearest_point(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
