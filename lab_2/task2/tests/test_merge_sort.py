import unittest
from lab_2.task2.src.task2 import mergeSort


class MergeSort(unittest.TestCase):
    def test_should_merge_sort(self):
        self.assertEqual(mergeSort([6, 2, 4, 1, 1, 7], 0, 5), [7, 6, 4, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()

