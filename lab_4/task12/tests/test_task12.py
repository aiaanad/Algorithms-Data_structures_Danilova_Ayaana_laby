import random
import time
import unittest
from lab_4.task12.src.task12 import main


class TestFormation(unittest.TestCase):
    def test_should_formation_args1(self):
        # given
        args = (3, 3, ['left', 2, 1], ['right', 3, 1], ['name', 1])
        expected_result = ['2 3']
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_formation_args2(self):
        # given
        args = (3, 4, ['left', 2, 1], ['right', 3, 1], ['leave', 1], ['name', 2])
        expected_result = ['0 3']
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
