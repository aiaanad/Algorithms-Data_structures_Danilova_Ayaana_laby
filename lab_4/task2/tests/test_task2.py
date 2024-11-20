import random
import time
import unittest
from lab_4.task2.src.task2 import realize_queue


class TestBugaboo(unittest.TestCase):
    def test_should_realize_queue_args1(self):
        # given
        data = (4, ['+', 1], ['+', 10], ['-'], ['-'])
        expected_result = [1, 10]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = realize_queue(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_realize_queue_args2(self):
        # given
        data = 5, 3, [1, 5, 3, 4, 1]
        expected_result = "ДА"
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = realize_queue(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
