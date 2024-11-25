import time
import unittest
from lab_5.task1.src.task1 import is_heap


class TestIsHeap(unittest.TestCase):
    def test_should_is_heap_args1(self):
        # given
        args = 5, [1, 0, 1, 2, 0]
        expected_result = "NO"
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_is_heap_args2(self):
        # given
        args = 5, [1, 3, 2, 5, 4]
        expected_result = "YES"
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_is_heap_max(self):
        # given
        args = 10**6, range(2*10**9 - 10**6, 2*10**9 + 1)
        expected_result = "YES"
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
