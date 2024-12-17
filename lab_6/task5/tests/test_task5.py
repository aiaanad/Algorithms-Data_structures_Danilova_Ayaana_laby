import unittest
import time
import tracemalloc
from lab_6.task5.src.task5 import main


class TestVoteCounting(unittest.TestCase):
    def test_should_count_vote_args1(self):
        # given
        args = (['ivanov', 100], ['ivanov', 500], ['ivanov', 300], ['petr', 70], ['tourist', 1], ['tourist', 2])
        expected_result = ['ivanov 900', 'petr 70', 'tourist 3']
        expected_time = 5
        expected_memory = 64

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

    def test_should_count_vote_args2(self):
        # given
        args = (['McCain', 10], ['McCain', 5], ['Obama', 9], ['Obama', 8], ['McCain', 1])
        expected_result = ['McCain 16', 'Obama 17']
        expected_time = 5
        expected_memory = 64

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


