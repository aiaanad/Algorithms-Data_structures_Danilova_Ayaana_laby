import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task3.src.task3 import inversion_number


class TestInversionNumber(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        self.expected1 = 17
        self.correct_check_args2 = 10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.expected2 = 45
        self.correct_check_args3 = 10, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        self.expected3 = 0

        self.max_args = 10 ** 5, random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        inversion_number(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_inversion_number_args1(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args1):
            self.assertEqual(inversion_number(*self.correct_check_args1), self.expected1)

    def test_should_inversion_number_args2(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args2):
            self.assertEqual(inversion_number(*self.correct_check_args2), self.expected2)

    def test_should_inversion_number_args3(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args3):
            self.assertEqual(inversion_number(*self.correct_check_args3), self.expected3)

    def test_should_anti_inversion_number_max_args(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
