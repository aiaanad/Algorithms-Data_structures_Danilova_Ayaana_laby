import random
import time
import unittest
from lab_3.task7.src.task7 import radix_sort


class TestRadixSort(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных."""
        self.array = [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        self.correct_check_args1 = (3, 3, 1)
        self.expected1 = [2, 3, 1]
        self.correct_check_args2 = 3, 3, 2
        self.expected2 = [3, 2, 1]
        self.correct_check_args3 = 3, 3, 3
        self.expected3 = [2, 3, 1]

    def check_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        radix_sort(*args, self.array)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_radix_sort_args1(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_args1)
        self.assertEqual(radix_sort(*self.correct_check_args1, self.array), self.expected1)

    def test_should_radix_sort_args2(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_args2)
        self.assertEqual(radix_sort(*self.correct_check_args2, self.array), self.expected2)

    def test_should_radix_sort_args3(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_args3)
        self.assertEqual(radix_sort(*self.correct_check_args3, self.array), self.expected3)


if __name__ == "__main__":
    unittest.main()
