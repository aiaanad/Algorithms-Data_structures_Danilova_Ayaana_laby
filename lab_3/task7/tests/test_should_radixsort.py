import unittest
from lab_3.task7.src.task7 import radix_sort


class RadixSort(unittest.TestCase):
    def test_should_radix_sort(self):
        a = [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        self.assertEqual(radix_sort(3, 3, 1, a), [2, 3, 1])
        self.assertEqual(radix_sort(3, 3, 2, a), [3, 2, 1])
        self.assertEqual(radix_sort(3, 3, 3, a), [2, 3, 1])


if __name__ == '__main__':
    unittest.main()

