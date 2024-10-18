import unittest
from lab_2.task8.src.task8 import polynomial_mult


class PolynomialMultTestCase(unittest.TestCase):
    def test_polynomial_mult(self):
        self.assertEqual(polynomial_mult(6, [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]),
                         [6, 17, 32, 50, 70, 91, 70, 50, 32, 17, 6])
        self.assertEqual(polynomial_mult(7, [3, 12, 34, 67, 89, 2, 4], [101, 2, 3, 1, 56, 11, 0]),
                         [303, 1218, 3467, 6874, 9405, 1320, 2778, 4229, 5735, 1095, 246, 44, 0])
        self.assertEqual(polynomial_mult(4, [1, 0, 1, 0], [0, 1, 0, 1]),
                         [0, 1, 0, 2, 0, 1, 0])

