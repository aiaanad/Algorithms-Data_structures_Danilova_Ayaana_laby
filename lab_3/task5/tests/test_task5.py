import random
import time
import unittest
from lab_3.task5.src.task5 import hirsh_index


class TestHirshIndex(unittest.TestCase):
    def test_should_hirsh_index_args1(self):
        # given
        data = [3, 0, 1, 6, 6], 0, 4
        expected_result = 3
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = hirsh_index(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_hirsh_index_args2(self):
        # given
        data = [1, 3, 1], 0, 2
        expected_result = 1
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = hirsh_index(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
