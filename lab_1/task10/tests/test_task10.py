import random
import time
import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.task10.src.task10 import palindrom


class TestPalindrom(unittest.TestCase):

    def setUp(self):
        """GIVEN: Подготовка тестовых данных."""
        self.correct_check_args = 6, ['Q', 'A', 'Z', 'Q', 'A', 'Z']
        self.expected = ['A', 'Q', 'Z', 'Z', 'Q', 'A']

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        palindrom(*args)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_palindrom(self):
        """THEN: результат должен быть корректным."""
        if self.check_performance(self.correct_check_args):
            self.assertEqual(palindrom(*self.correct_check_args), self.expected)


if __name__ == "__main__":
    unittest.main()
