import random
import time
import unittest
import psutil
from lab_4.task9.src.task9 import (main)


class TestClinic(unittest.TestCase):
    def test_should_clinic_args1(self):
        # given
        args = (7, ['+', 1], ['+', 2], ['-'], ['+', 3], ['+', 4], ['-'], ['-'])
        expected_result = [1, 2, 3]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_clinic_args2(self):
        # given
        args = (10, ['+', 1], ['+', 2], ['*', 3], ['-'], ['+', 4], ['*', 5], ['-'], ['-'], ['-'], ['-'])
        expected_result = [1, 3, 2, 5, 4]
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f'Итоговое время алгоритма: {result_time} секунд \n'
              f'Итоговая затрата памяти:: {memory} МБ')

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_clinic_max_args(self):
        # given
        args = (10**5,)
        expected_result = []
        expected_time = 60
        expected_memory = 256

        actions = ['+', '*', '-']
        arr = []
        for i in range(1, 10**5 + 1):
            act = random.choice(actions)
            match act:
                case '+':
                    arr.append(i)
                    args += (['+', i],)
                case '*':
                    args += (['*', i],)
                    arr.insert((len(arr)+1) // 2, i)
                case '-':
                    args += (['-'],)
                    if arr:
                        expected_result.append(arr.pop(0))
                    else:
                        expected_result.append(None)

        # when
        start_time = time.perf_counter()
        result = main(*args)
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