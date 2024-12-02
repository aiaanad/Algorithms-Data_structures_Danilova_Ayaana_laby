import unittest
import psutil
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
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

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
        result = MinHeap(data[0], data[1]).heap_sort()
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

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
        result = MinHeap(*args).heap_sort()
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")
