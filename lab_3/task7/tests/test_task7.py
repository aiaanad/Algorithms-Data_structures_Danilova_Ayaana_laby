import time
import unittest
from lab_3.task7.src.task7 import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_should_radix_sort_args1(self):
        # given
        data = 3, 3, 1, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [2, 3, 1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_radix_sort_args2(self):
        # given
        data = 3, 3, 2, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [3, 2, 1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_radix_sort_args3(self):
        # given
        data = 3, 3, 3, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [2, 3, 1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
