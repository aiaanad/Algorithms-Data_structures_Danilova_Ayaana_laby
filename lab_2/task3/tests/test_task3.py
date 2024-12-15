import time
import unittest
import tracemalloc
from lab_2.task3.src.task3 import inversion_number


class TestInversionNumber(unittest.TestCase):
    def test_should_inversion_number(self):
        # given
        data = 10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_result = 17
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = inversion_number(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        inversion_number(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
