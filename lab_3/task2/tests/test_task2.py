import time
import unittest
from lab_3.task2.src.task2 import anti_qsort


class TestAntiQSort(unittest.TestCase):
    def test_should_anti_qsort_n1(self):
        # given
        data = 3
        expected_result = [1, 3, 2]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = anti_qsort(data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_anti_qsort_n2(self):
        # given
        data = 6
        expected_result = [1, 4, 6, 3, 2, 5]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = anti_qsort(data)
        result_time = time.perf_counter() - start_time
        print("Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
