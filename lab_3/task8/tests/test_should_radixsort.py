import unittest
from lab_3.task8.src.task8 import nearest_point


class NearestPoint(unittest.TestCase):
    def test_should_nearest_point(self):
        self.assertEqual(nearest_point(2, 1, [[1, 3], [-2, 2]]), [[-2, 2]])
        self.assertEqual(nearest_point(3, 2, [[3, 3], [5, -1], [-2, 4]]), [[3, 3], [-2, 4]])


if __name__ == '__main__':
    unittest.main()

