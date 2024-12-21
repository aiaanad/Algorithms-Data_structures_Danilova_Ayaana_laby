import time
import unittest
import tracemalloc
from lab_3.task3.src.task3 import bugaboo


class TestBugaboo(unittest.TestCase):
    def test_should_bugaboo_args1(self):
        # given
        data = [3, 2], [2, 1, 3]
        expected_result = "НЕТ"
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = bugaboo(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        bugaboo(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_bugaboo_args2(self):
        # given
        data = [5, 3], [1, 5, 3, 4, 1]
        expected_result = "ДА"
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = bugaboo(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        bugaboo(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
