import time
import unittest
import tracemalloc
from lab_2.task8.src.task8 import polynomial_mult


class TestPolynomialMultiplication(unittest.TestCase):
    def test_should_polynomial_mult_args1(self):
        # given
        data = 6, [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]
        expected_result = [6, 17, 32, 50, 70, 91, 70, 50, 32, 17, 6]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = polynomial_mult(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        polynomial_mult(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_polynomial_mult_args2(self):
        # given
        data = 7, [3, 12, 34, 67, 89, 2, 4], [101, 2, 3, 1, 56, 11, 0]
        expected_result = [303, 1218, 3467, 6874, 9405, 1320, 2778, 4229, 5735, 1095, 246, 44, 0]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = polynomial_mult(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        polynomial_mult(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_polynomial_mult_args3(self):
        # given
        data = 4, [1, 0, 1, 0], [0, 1, 0, 1]
        expected_result = [0, 1, 0, 2, 0, 1, 0]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = polynomial_mult(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        polynomial_mult(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
