import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task7.src.task7 import sortland


class TestSortLand(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 5, [10.00, 8.70, 0.01, 5.00, 3.00]
        self.expected1 = (3, 4, 1)

        self.max_args = 10 ** 4, random.sample(range(10 ** 9), 10 ** 4)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        sortland(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_sortland_args1(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args1):
            self.assertEqual(sortland(*self.correct_check_args1), self.expected1)

    def test_should_sortland_max_args(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
