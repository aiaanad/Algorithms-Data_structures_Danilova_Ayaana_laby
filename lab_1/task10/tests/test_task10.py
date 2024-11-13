import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task10.src.task10 import palindrom


class TestPalindrom(unittest.TestCase):
    def test_should_palindrom(self):
        # given
        data = 6, ['Q', 'A', 'Z', 'Q', 'A', 'Z']
        expected_result = 'AQZZQA'
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = palindrom(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
