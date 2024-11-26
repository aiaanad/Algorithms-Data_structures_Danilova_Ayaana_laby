import random
import time
import unittest
from lab_4.task9.src.task9 import (main)


class TestClinic(unittest.TestCase):
    def test_should_clinic_args1(self):
        # given
        args = (7, ['+', 1], ['+', 2], ['-'], ['+', 3], ['+', 4], ['-'], ['-'])
        expected_result = [1, 2, 3]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_clinic_args2(self):
        # given
        args = (10, ['+', 1], ['+', 2], ['*', 3], ['-'], ['+', 4], ['*', 5], ['-'], ['-'], ['-'], ['-'])
        expected_result = [1, 3, 2, 5, 4]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()