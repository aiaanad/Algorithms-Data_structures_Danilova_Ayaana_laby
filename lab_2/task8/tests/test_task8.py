import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task8.src.task8 import polynomial_mult


class TestPolynomialMultiplication(unittest.TestCase):
    def test_should_polynomial_mult_args1(self):
        # given
        data = 6, [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]
        expected_result = [6, 17, 32, 50, 70, 91, 70, 50, 32, 17, 6]

        # when
        result = polynomial_mult(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_polynomial_mult_args2(self):
        # given
        data = 7, [3, 12, 34, 67, 89, 2, 4], [101, 2, 3, 1, 56, 11, 0]
        expected_result = [303, 1218, 3467, 6874, 9405, 1320, 2778, 4229, 5735, 1095, 246, 44, 0]

        # when
        result = polynomial_mult(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_polynomial_mult_args3(self):
        # given
        data = 4, [1, 0, 1, 0], [0, 1, 0, 1]
        expected_result = [0, 1, 0, 2, 0, 1, 0]

        # when
        result = polynomial_mult(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
