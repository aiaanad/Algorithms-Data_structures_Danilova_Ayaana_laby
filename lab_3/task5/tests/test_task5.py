import random
import time
import unittest
from lab_3.task5.src.task5 import hirsh_index


class TestHirshIndex(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных."""
        self.correct_check_args1 = [3, 0, 1, 6, 6], 0, 4
        self.expected1 = 3
        self.correct_check_args2 = [1, 3, 1], 0, 2
        self.expected2 = 1

        self.max_args = random.sample(range(10 ** 9), 10 ** 4), 0, 9999

    def time_performance(self, args):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        hirsh_index(*args)
        execution_time = time.perf_counter() - time_start
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_hirsh_index_args1(self):
        """THEN: результат должен быть корректным."""
        self.time_performance(self.correct_check_args1)
        self.assertEqual(hirsh_index(*self.correct_check_args1), self.expected1)

    def test_should_hirsh_index_args2(self):
        """THEN: результат должен быть корректным."""
        self.time_performance(self.correct_check_args2)
        self.assertEqual(hirsh_index(*self.correct_check_args2), self.expected2)

    def test_should_anti_hirsh_index_max_args(self):
        """THEN: время для максимального n."""
        self.time_performance(self.max_args)


if __name__ == "__main__":
    unittest.main()
