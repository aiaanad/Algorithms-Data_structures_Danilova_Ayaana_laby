import time
import unittest
import tracemalloc
from lab_1.task7.src.task7 import sortland


class TestSortLand(unittest.TestCase):
    def test_should_sort_land(self):
        # given
        data = 5, [10.00, 8.70, 0.01, 5.00, 3.00]
        expected_result = (3, 4, 1)
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = sortland(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        sortland(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
