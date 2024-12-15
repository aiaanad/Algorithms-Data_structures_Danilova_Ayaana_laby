import time
import unittest
import tracemalloc
from lab_3.task2.src.task2 import anti_qsort


class TestAntiQSort(unittest.TestCase):
    def test_should_anti_qsort_n1(self):
        # given
        data = 3
        expected_result = [1, 3, 2]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = anti_qsort(data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        anti_qsort(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_anti_qsort_n2(self):
        # given
        data = 6
        expected_result = [1, 4, 6, 3, 2, 5]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = anti_qsort(data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        anti_qsort(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
