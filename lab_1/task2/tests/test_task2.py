import unittest
import time
import tracemalloc
from lab_1.task2.src.task2 import insertion_sort_plus


class TestInsertionSortPlus(unittest.TestCase):
    def test_should_sort_plus(self):
        # given
        data = 10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_result = [1, 2, 2, 2, 3, 5, 5, 6, 9, 1]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = insertion_sort_plus(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        insertion_sort_plus(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
