import time
import tracemalloc
import unittest
from lab_1.task9.src.task9 import binary_addition


class TestBinaryAddition(unittest.TestCase):
    def test_should_binary_addition(self):
        # given
        data = [1, 1, 0, 0], [1, 0, 1, 1]
        expected_result = [1, 0, 1, 1, 1]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = binary_addition(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        binary_addition(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
