import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task5.src.task5 import majority


class TestMajority(unittest.TestCase):
    def test_should_majority(self):
        # given
        data = 6, [1, 3, 6, 1, 8, 1]
        expected_result = 0
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = majority(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
