import unittest
from lab_3.task1.src.task1 import randomized_quicksort


class Quicksort(unittest.TestCase):
    def test_should_quicksort(self):
        self.assertEqual(randomized_quicksort([6, 2, 4, 1, 1, 7], 0, 5), [1, 1, 2, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()

