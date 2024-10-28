import unittest
from lab_2.task3.src.task3 import inversion_number


class InversionNumberTestCase(unittest.TestCase):

    def test_should_inversion_number(self):
        self.assertEqual(inversion_number(10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]), 17)
        self.assertEqual(inversion_number(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
        self.assertEqual(inversion_number(10, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 0)
        self.assertEqual(inversion_number(10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 45)


if __name__ == '__main__':
    unittest.main()
