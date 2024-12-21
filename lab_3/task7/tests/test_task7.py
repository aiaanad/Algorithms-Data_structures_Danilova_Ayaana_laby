import time
import unittest
import tracemalloc
from lab_3.task7.src.task7 import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_should_radix_sort_args1(self):
        # given
        data = [3, 3, 1], 'bbb', 'aba', 'baa'
        expected_result = [2, 3, 1]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        radix_sort(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_radix_sort_args2(self):
        # given
        data = [3, 3, 2], 'bbb', 'aba', 'baa'
        expected_result = [3, 2, 1]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        radix_sort(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_radix_sort_args3(self):
        # given
        data = [3, 3, 3], 'bbb', 'aba', 'baa'
        expected_result = [2, 3, 1]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = radix_sort(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        radix_sort(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
