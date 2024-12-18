import time
import unittest
import random
import tracemalloc
from lab_7.task6.src.task6 import lis


class TestHashTable(unittest.TestCase):
    def test_should_find_increase_seq_args1(self):
        # given
        args = (6, [3, 29, 5, 5, 28, 1])
        expected_result = (3, '3 5 28')
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = lis(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        lis(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_find_increase_seq_max_args(self):
        # given
        n = 5000
        arr = [_ for _ in range(10 ** 8, 10 ** 8 + n)]
        expected_result = (len(arr), ' '.join(map(str, arr)))

        args = (n, arr)
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = lis(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        lis(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
