import random
import time
import tracemalloc
import unittest
from lab_1.task1.src.task1 import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_should_sort_small_array(self):
        # given
        data = random.sample(range(10 ** 5), 10 ** 2)
        expected_result = sorted(data)
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = insertion_sort(len(data), data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        insertion_sort(len(data), data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_sort_large_array(self):
        # given
        data = random.sample(range(10 ** 9), 10 ** 4)
        expected_result = sorted(data)
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = insertion_sort(len(data), data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        insertion_sort(len(data), data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
