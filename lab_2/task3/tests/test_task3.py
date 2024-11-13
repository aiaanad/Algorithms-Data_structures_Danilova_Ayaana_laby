import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task3.src.task3 import inversion_number


class TestInversionNumber(unittest.TestCase):
    def test_should_inversion_number(self):
        # given
        data = 10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_result = 17
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = inversion_number(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
