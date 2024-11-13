import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task9.src.task9 import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_should_binary_addition(self):
        # given
        data = [1, 1, 0, 0], [1, 0, 1, 1]
        expected_result = [1, 0, 1, 1, 1]

        # when
        result = binary_addition(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
