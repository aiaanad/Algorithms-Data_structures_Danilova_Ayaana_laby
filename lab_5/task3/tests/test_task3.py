import unittest
import psutil
import time
from lab_5.task3.src.task3 import processing_net_packets
from random import randint


class TestNetworkPacketProcessing(unittest.TestCase):

    def test_should_processing_args1(self):

        # given
        args = (3, 6, [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2])
        expected_result = [0, 2, 4, 6, 8, -1]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = processing_net_packets(*args)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ'
              f'')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_processing_args2(self):
        # given
        args = (2, 3, [0, 1], [3, 1], [10, 1])
        expected_result = [0, 3, 10]
        expected_time = 2

        # when
        start_time = time.perf_counter()
        result = processing_net_packets(*args)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_processing_max_args(self):
        # given
        expected_time = 10
        args = (10**3, 10**5)
        packages = [[c + 10, randint(0, 10**3)] for c in range(10**5)]
        for pair in sorted(packages):
            args += (pair,)

        # when
        start_time = time.perf_counter()
        result = processing_net_packets(*args)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()