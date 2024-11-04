import unittest
from lab_3.task3.src.task3 import bugaboo


class Bugaboo(unittest.TestCase):
    def test_should_bugaboo(self):
        self.assertEqual(bugaboo(3, 2, [2, 1, 3]), 'НЕТ')
        self.assertEqual(bugaboo(5, 3, [1, 5, 3, 4, 1]), 'ДА')
        self.assertEqual(bugaboo(10, 3, [4, 2, 5, 3, 1, 6, 2, 1, 4, 1]), 'НЕТ')


if __name__ == '__main__':
    unittest.main()

