import unittest
from lab_3.task5.src.task5 import hirsh_index


class HirshIndex(unittest.TestCase):
    def test_should_bugaboo(self):
        self.assertEqual(hirsh_index([3, 0, 1, 6, 6], 0, 4), 3)
        self.assertEqual(hirsh_index([1, 3,1], 0, 2), 1)
        self.assertEqual(hirsh_index([3, 3, 3, 4, 4, 4, 4], 0, 6), 4)
        self.assertEqual(hirsh_index([3, 3, 3, 4, 4, 4], 0, 5), 3)


if __name__ == '__main__':
    unittest.main()

