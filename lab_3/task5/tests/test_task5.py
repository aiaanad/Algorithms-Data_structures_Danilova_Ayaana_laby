import time
import unittest
import psutil
from lab_3.task5.src.task5 import hirsh_index


class TestHirshIndex(unittest.TestCase):
    def test_should_hirsh_index_args1(self):
        # given
        data = [3, 0, 1, 6, 6], 0, 4
        expected_result = 3
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = hirsh_index(*data)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_hirsh_index_args2(self):
        # given
        data = [1, 3, 1], 0, 2
        expected_result = 1
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = hirsh_index(*data)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
