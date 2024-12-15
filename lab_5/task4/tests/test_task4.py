import unittest
import tracemalloc
import time
from lab_5.task4.src.task4 import MinHeap
from random import randint


class TestHeapSortSwaps(unittest.TestCase):
    def test_should_heapsort_args1(self):
        # given
        expected_time = 2
        expected_memory = 256
        data = (5, [1, 2, 3, 4, 5])
        expected_result = (0, [])

        # when
        start_time = time.perf_counter()
        result = MinHeap(*data).heap_sort()
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        MinHeap(*data).heap_sort()
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heapsort_args2(self):
        # given
        expected_time = 2
        expected_memory = 256
        data = (5, [5, 4, 3, 2, 1])
        expected_result = (3, [(1, 4), (0, 1), (1, 3)])

        # when
        start_time = time.perf_counter()
        result = MinHeap(*data).heap_sort()
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        MinHeap(*data).heap_sort()
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heapsort_max_args(self):
        # given
        expected_time = 2
        expected_memory = 256
        array = [randint(0, 10**9) for _ in range(10**5 + 10)]
        array = [i for i in set(array)]
        args = (len(array), array)

        # when
        start_time = time.perf_counter()
        MinHeap(*args).heap_sort()
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        MinHeap(*args).heap_sort()
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")
