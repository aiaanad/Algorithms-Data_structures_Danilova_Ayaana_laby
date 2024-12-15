import time
import unittest
import tracemalloc
from lab_2.task5.src.task5 import majority


class TestMajority(unittest.TestCase):
    def test_should_majority(self):
        # given
        data = 6, [1, 3, 6, 1, 8, 1]
        expected_result = 0
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = majority(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        majority(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
