import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task10.src.task10 import palindrom


class TestPalindrom(unittest.TestCase):
    def test_should_palindrom(self):
        # given
        data = 6, ['Q', 'A', 'Z', 'Q', 'A', 'Z']
        expected_result = ['A', 'Q', 'Z', 'Z', 'Q', 'A']

        # when
        result = palindrom(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
