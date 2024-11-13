import random
import time
import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task4.src.task4 import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_should_binary_search(self):
        # given
        data = 5, [1, 5, 8, 12, 13], 5, [8, 1, 23, 1, 11]
        expected_result = [2, 0, -1, 0, -1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = binary_search(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
