import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_3.task1.src.task1 import randomized_quicksort


class TestRandomizedQuicksort(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.small_arr = random.sample(range(10 ** 5), 10 ** 2)
        self.large_arr = random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, array):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        randomized_quicksort(array.copy(), 0, len(array) - 1)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_sort_small_array(self):
        """THEN: результат должен быть отсортированным массивом."""
        if self.check_performance(self.small_arr):
            self.assertEqual(randomized_quicksort(self.small_arr, 0, len(self.small_arr) - 1), sorted(self.small_arr))

    def test_should_sort_large_array(self):
        """THEN: результат должен быть отсортированным массивом."""
        if self.check_performance(self.large_arr):
            self.assertEqual(randomized_quicksort(self.large_arr, 0, len(self.large_arr) - 1), sorted(self.large_arr))


if __name__ == "__main__":
    unittest.main()
