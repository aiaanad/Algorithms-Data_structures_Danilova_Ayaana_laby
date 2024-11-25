import random
import time
import unittest
from lab_3.task1.src.task1 import randomized_quicksort


class TestRandomizedQuicksort(unittest.TestCase):
    def test_should_sort_small_array(self):
        # given
        data = random.sample(range(10 ** 5), 10 ** 2)
        expected_result = sorted(data)
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = randomized_quicksort(data, 0, len(data) - 1)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_array(self):
        # given
        data = random.sample(range(10 ** 9), 10 ** 4)
        expected_result = sorted(data)
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = randomized_quicksort(data, 0, len(data) - 1)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
