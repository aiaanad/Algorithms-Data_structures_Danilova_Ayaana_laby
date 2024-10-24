import unittest
from lab_2.task1.src.task1 import mergeSort


class MergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(mergeSort([6, 2, 4, 1, 1, 7], 0, 5), [1, 1, 2, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()