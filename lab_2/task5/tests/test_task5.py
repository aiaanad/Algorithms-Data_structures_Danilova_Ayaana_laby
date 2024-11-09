import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task5.src.task5 import majority


class TestMajority(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 6, [1, 3, 6, 1, 8, 1]
        self.expected1 = 0
        self.correct_check_args2 = 6, [1, 3, 1, 1, 8, 1]
        self.expected2 = 1

        self.max_args = 10 ** 5, random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        majority(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_majority_args1(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args1):
            self.assertEqual(majority(*self.correct_check_args1), self.expected1)

    def test_should_majority_args2(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args2):
            self.assertEqual(majority(*self.correct_check_args2), self.expected2)

    def test_should_majority_max_args(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
