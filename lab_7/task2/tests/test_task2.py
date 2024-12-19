import unittest
import time
import tracemalloc
from lab_7.task2.src.task2 import simple_calculator


class TestSimpleCalculator(unittest.TestCase):
    def test_should_calculate_1(self):
        # given
        args = (1,)
        expected_result = (0, 1)
        expected_time = 1
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = simple_calculator(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        simple_calculator(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_calculate_args1(self):
        # given
        args = (96234,)
        expected_result = (14, '1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234')
        expected_time = 1
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = simple_calculator(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        simple_calculator(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_calculate_max_args(self):
        # given
        args = (10 ** 5,)
        expected_time = 1
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = simple_calculator(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        simple_calculator(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
