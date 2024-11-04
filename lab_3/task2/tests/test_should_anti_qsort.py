import unittest
from lab_3.task2.src.task2 import anti_qsort


class AntiQSort(unittest.TestCase):
    def test_should_anti_qsort(self):
        self.assertEqual(anti_qsort(3), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()

