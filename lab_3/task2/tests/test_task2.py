import random
import time
import unittest
from lab_3.task2.src.task2 import anti_qsort


class TestAntiQSort(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных."""
        self.correct_check_val1, self.expected1 = 3, [1, 3, 2]
        self.correct_check_val2, self.expected2 = 6, [1, 4, 6, 3, 2, 5]

        self.max_n = 10 ** 6

    def check_performance(self, n):
        """WHEN: Проверка производительности: время выполнения."""
        time_start = time.perf_counter()
        anti_qsort(n)
        execution_time = time.perf_counter() - time_start

        if execution_time > 2:
            self.fail(f"Время выполнения превышает 2 секунды: {execution_time} секунд")
        print(f"Время выполнения: {execution_time} секунд")

    def test_should_anti_qsort_n1(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_val1)
        self.assertEqual(anti_qsort(self.correct_check_val1), self.expected1)

    def test_should_anti_qsort_n2(self):
        """THEN: результат должен быть корректным."""
        self.check_performance(self.correct_check_val2)
        self.assertEqual(anti_qsort(self.correct_check_val2), self.expected2)

    def test_should_anti_qsort_max_n(self):
        """THEN: время для максимального n."""
        self.check_performance(self.max_n)


if __name__ == "__main__":
    unittest.main()
