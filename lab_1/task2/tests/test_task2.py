import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task2.src.task2 import insertion_sort_plus


class TestInsertionSortPlus(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.args = 10, [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        self.expected = [1, 2, 2, 2, 3, 5, 5, 6, 9, 1]
        self.args_max = 10 ** 5, random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        insertion_sort_plus(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 3:
            self.fail(f"Время выполнения превышает 3 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_sort_plus(self):
        """THEN: результат должен быть отсортированным массивом."""
        if self.check_performance(self.args):
            self.assertEqual(insertion_sort_plus(*self.args), self.expected)

    def test_should_sort_plus_max(self):
        """THEN: результат должен быть отсортированным массивом."""
        self.check_performance(self.args_max)


if __name__ == "__main__":
    unittest.main()
