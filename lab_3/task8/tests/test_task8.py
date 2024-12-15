import time
import unittest
import tracemalloc
from lab_3.task8.src.task8 import nearest_point


class TestNearestPoint(unittest.TestCase):
    def test_should_nearest_point_args1(self):
        # given
        data = 2, 1, [[1, 3], [-2, 2]]
        expected_result = [[-2, 2]]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = nearest_point(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        nearest_point(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_nearest_point_args2(self):
        # given
        data = 3, 2, [[3, 3], [5, -1], [-2, 4]]
        expected_result = [[3, 3], [-2, 4]]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = nearest_point(*data)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        nearest_point(*data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
