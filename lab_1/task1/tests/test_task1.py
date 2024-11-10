import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task1.src.task1 import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.small_arr = random.sample(range(10 ** 5), 10 ** 2)
        self.large_arr = random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, array):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        insertion_sort(len(array), array.copy())
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_sort_small_array(self):
        """THEN: результат должен быть отсортированным массивом."""
        if self.check_performance(self.small_arr):
            self.assertEqual(insertion_sort(len(self.small_arr), self.small_arr), sorted(self.small_arr))

    def test_should_sort_large_array(self):
        """THEN: результат должен быть отсортированным массивом."""
        if self.check_performance(self.large_arr):
            self.assertEqual(insertion_sort(len(self.large_arr), self.large_arr), sorted(self.large_arr))


if __name__ == "__main__":
    unittest.main()
