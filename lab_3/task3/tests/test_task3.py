import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_3.task3.src.task3 import bugaboo


class TestBugaboo(unittest.TestCase):
    def test_should_bugaboo_args1(self):
        # given
        data = 3, 2, [2, 1, 3]
        expected_result = "НЕТ"

        # when
        result = bugaboo(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_bugaboo_args2(self):
        # given
        data = 5, 3, [1, 5, 3, 4, 1]
        expected_result = "ДА"

        # when
        result = bugaboo(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
