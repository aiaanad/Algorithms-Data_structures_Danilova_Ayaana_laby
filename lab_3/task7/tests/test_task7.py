import time
import unittest
from lab_3.task7.src.task7 import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_should_radix_sort_args1(self):
        # given
        data = 3, 3, 1, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [2, 3, 1]

        # when
        result = radix_sort(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_radix_sort_args2(self):
        # given
        data = 3, 3, 2, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [3, 2, 1]

        # when
        result = radix_sort(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_radix_sort_args3(self):
        # given
        data = 3, 3, 2, [['b', 'b', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
        expected_result = [2, 3, 1]

        # when
        result = radix_sort(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
