import random
import time
import unittest
from lab_4.task5.src.task5 import main


class TestStackWithMax(unittest.TestCase):
    def test_should_stack_with_max_args1(self):
        # given
        args = (5, ['push', 2], ['push', 1], ['max'], ['pop'], ['max'])
        expected_result = [2, 2]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()