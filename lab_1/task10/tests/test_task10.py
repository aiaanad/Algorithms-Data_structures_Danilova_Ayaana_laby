import time
import unittest
import tracemalloc
from lab_1.task10.src.task10 import palindrome


class TestPalindrom(unittest.TestCase):
    def test_should_palindrom(self):
        # given
        data = 6, ['Q', 'A', 'Z', 'Q', 'A', 'Z']
        expected_result = 'AQZZQA'
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = palindrome(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        palindrome(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
