import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_2.task8.src.task8 import polynomial_mult


class TestPolynomialMultiplication(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args1 = 6, [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]
        self.expected1 = [6, 17, 32, 50, 70, 91, 70, 50, 32, 17, 6]
        self.correct_check_args2 = 7, [3, 12, 34, 67, 89, 2, 4], [101, 2, 3, 1, 56, 11, 0]
        self.expected2 = [303, 1218, 3467, 6874, 9405, 1320, 2778, 4229, 5735, 1095, 246, 44, 0]
        self.correct_check_args3 = 4, [1, 0, 1, 0], [0, 1, 0, 1]
        self.expected3 = [0, 1, 0, 2, 0, 1, 0]

        self.max_args = 10 ** 5, random.sample(range(10 ** 9), 10 ** 5), random.sample(range(10 ** 9), 10 ** 5)

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        polynomial_mult(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 3:
            self.fail(f"Время выполнения превышает 3 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_polynomial_mult_args1(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args1):
            self.assertEqual(polynomial_mult(*self.correct_check_args1), self.expected1)

    def test_should_polynomial_mult_args2(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args2):
            self.assertEqual(polynomial_mult(*self.correct_check_args2), self.expected2)

    def test_should_polynomial_mult_args3(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args3):
            self.assertEqual(polynomial_mult(*self.correct_check_args3), self.expected3)

    def test_should_polynomial_mult_max_args(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
