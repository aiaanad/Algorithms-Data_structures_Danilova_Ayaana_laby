import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task3.src.task3 import inversion_number


class TestInversionNumber(unittest.TestCase):
    def test_should_inversion_number(self):
        # given
        data = 10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_result = 17

        # when
        result = inversion_number(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
