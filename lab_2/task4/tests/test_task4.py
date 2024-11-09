import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task4.src.task4 import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 6, [1, 1, 3, 4, 5, 6], 3, [1, 2, 5]
        self.expected1 = [0, -1, 4]

        self.max_args = 10 ** 5, random.sample(range(10 ** 9), 10 ** 5), 10 ** 5, random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        binary_search(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_binary_search_args1(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args1):
            self.assertEqual(binary_search(*self.correct_check_args1), self.expected1)

    def test_should_binary_search_max_args(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
