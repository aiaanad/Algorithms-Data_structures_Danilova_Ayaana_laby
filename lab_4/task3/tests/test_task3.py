import random
import time
import unittest
from lab_4.task3.src.task3 import bracket_sequence


class TestBracketSequence(unittest.TestCase):
    def test_should_bracket_sequence_args1(self):
        # given
        args = (2, ['([])([()]([]))'], ['[[())()]]'])
        expected_result = ['YES', 'NO']
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = bracket_sequence(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
