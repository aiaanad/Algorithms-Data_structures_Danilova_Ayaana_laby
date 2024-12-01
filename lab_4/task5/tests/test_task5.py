import random
import time
import unittest
from lab_4.task5.src.task5 import main


class TestStackWithMax(unittest.TestCase):
    def test_should_check_stack_with_args_from_task(self):
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

    def test_should_check_stack_with_big_args(self):
        # given
        args = (4 * 10**4,)
        expected_result = []
        expected_time = 5

        actions = ['push', 'max', 'pop']
        arr = []
        for i in range(4 * 10**4):
            act = random.choice(actions)
            match act:
                case 'push':
                    val = random.sample(range(10**5), 1)
                    arr.append(val)
                    args += (['push', val],)
                case 'pop':
                    args += (['pop'],)
                    if arr:
                        arr.pop()
                case 'max':
                    args += (['max'],)
                    if arr:
                        expected_result.append(max(arr))
                    else:
                        expected_result.append(None)

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