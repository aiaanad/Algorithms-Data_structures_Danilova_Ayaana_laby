import time
import unittest
import random
import string
import tracemalloc
from lab_7.task7.src.task7 import main


class TestIsMatch(unittest.TestCase):

    def test_should_check_match_with_empty_args(self):
        # given
        args = ([''], [''])
        expected_result = 'YES'
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_check_match_with_args1(self):
        # given
        args = (['k?t?n'], ['kitten'])
        expected_result = 'NO'
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_check_match_with_max_args(self):
        # given
        word = ''.join(random.choices(string.ascii_letters, k=10 ** 3 - 2))
        pattern = '*' * (10 ** 3 - 2)
        args = (pattern, [f'k{word}n'])
        expected_result = 'YES'
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
