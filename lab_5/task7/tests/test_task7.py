import time
import unittest
import tracemalloc
from lab_5.task7.src.task7 import heapsort


class TestHeaSort(unittest.TestCase):
    def test_should_heapsort_small_arr(self):
        # given
        args = 10**3, [10**9 - i for i in range(10**3)]
        expected_result = sorted(args[1])
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = heapsort(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        heapsort(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heapsort_middle_arr(self):
        # given
        expected_time = 2
        expected_memory = 256
        args = 10 ** 4, [10 ** 9 - i for i in range(10 ** 4)]
        expected_result = sorted(args[1])

        # when
        start_time = time.perf_counter()
        result = heapsort(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        heapsort(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heapsort_big_arr(self):
        # given
        expected_time = 2
        expected_memory = 256
        args = 10 ** 5, [10 ** 9 - i for i in range(10 ** 5)]
        expected_result = sorted(args[1])

        # when
        start_time = time.perf_counter()
        result = heapsort(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        heapsort(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
