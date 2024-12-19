import unittest
import time
import tracemalloc
import random
from lab_7.task1.src.task1 import coin_exchange


class TestCoinExchange(unittest.TestCase):
    def test_should_coin_exchange_args1(self):
        # given
        args = (40, 4, [25, 20, 10, 5])
        expected_result = 2
        expected_time = 1
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = coin_exchange(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        coin_exchange(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_coin_exchange_max_args(self):
        # given
        args = (10 ** 3, 100, random.sample(range(1, 10 ** 3 + 1), 100))
        expected_time = 1
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = coin_exchange(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        coin_exchange(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
