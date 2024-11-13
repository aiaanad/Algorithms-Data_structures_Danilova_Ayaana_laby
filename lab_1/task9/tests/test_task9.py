import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task9.src.task9 import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_should_binary_addition(self):
        # given
        data = [1, 1, 0, 0], [1, 0, 1, 1]
        expected_result = [1, 0, 1, 1, 1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = binary_addition(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
