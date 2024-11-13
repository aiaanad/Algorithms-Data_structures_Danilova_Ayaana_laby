import random
import time
import unittest
from lab_3.task5.src.task5 import hirsh_index


class TestHirshIndex(unittest.TestCase):
    def test_should_hirsh_index_args1(self):
        # given
        data = [3, 0, 1, 6, 6], 0, 4
        expected_result = 3

        # when
        result = hirsh_index(*data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_hirsh_index_args2(self):
        # given
        data = [1, 3, 1], 0, 2
        expected_result = 1

        # when
        result = hirsh_index(*data)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
