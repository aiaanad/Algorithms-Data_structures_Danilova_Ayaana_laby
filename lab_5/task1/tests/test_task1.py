import time
import unittest
import tracemalloc
from lab_5.task1.src.task1 import is_heap


class TestIsHeap(unittest.TestCase):
    def test_should_is_heap_args1(self):
        # given
        args = 5, [1, 0, 1, 2, 0]
        expected_result = "NO"
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        is_heap(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_is_heap_args2(self):
        # given
        args = 5, [1, 3, 2, 5, 4]
        expected_result = "YES"
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        is_heap(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_is_heap_max(self):
        # given
        args = 10**6, range(2*10**9 - 10**6, 2*10**9 + 1)
        expected_result = "YES"
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = is_heap(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        is_heap(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
