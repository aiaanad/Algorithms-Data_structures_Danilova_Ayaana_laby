import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_3.task8.src.task8 import nearest_point


class TestRadixSort(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 2, 1, [[1, 3], [-2, 2]]
        self.expected1 = [[-2, 2]]
        self.correct_check_args2 = 3, 2, [[3, 3], [5, -1], [-2, 4]]
        self.expected2 = [[3, 3], [-2, 4]]
        self.max_args = (10 ** 5, 99999, [random.sample(range(-10 ** 9, 10 ** 9), 2) for _ in range(10 ** 5)])

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        nearest_point(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 10:
            self.fail(f"Время выполнения превышает 10 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_nearest_point_args1(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_args1)
        self.assertEqual(nearest_point(*self.correct_check_args1), self.expected1)

    def test_should_nearest_point_args2(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_args2)
        self.assertEqual(nearest_point(*self.correct_check_args2), self.expected2)

    def test_should_nearest_point_max_args(self):
        """THEN: время для максимальных значений."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
