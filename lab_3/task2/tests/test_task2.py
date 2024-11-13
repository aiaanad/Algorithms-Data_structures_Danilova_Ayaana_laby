import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_3.task2.src.task2 import anti_qsort


class TestAntiQSort(unittest.TestCase):
    def test_should_anti_qsort_n1(self):
        # given
        data = 3
        expected_result = [1, 3, 2]

        # when
        result = anti_qsort(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_anti_qsort_n2(self):
        # given
        data = 6
        expected_result = [1, 4, 6, 3, 2, 5]

        # when
        result = anti_qsort(data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
