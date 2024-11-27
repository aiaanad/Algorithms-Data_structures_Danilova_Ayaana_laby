import random
import time
import unittest
from lab_4.task3.src.task3 import bracket_sequence


class TestBracketSequence(unittest.TestCase):
    def test_should_check_args_from_task(self):
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

    def test_should_check_balanced_brackets_sequence(self):
        # given
        seq = ['([])'] * (10 ** 4 // 2)
        args = (500,)
        args += tuple([seq for i in range(500)])
        expected_result = ['YES'] * 500
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = bracket_sequence(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_not_balanced_brackets_sequence(self):
        # given
        seq = ['([]('] * (10 ** 4 // 2)
        args = (500,)
        args += tuple([seq for i in range(500)])
        expected_result = ['NO'] * 500
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
