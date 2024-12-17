import unittest
from lab_6.task3.src.task3 import HashTableChaining


class TestHashTableChaining(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTableChaining(5)

    def test_should_add_and_find(self):
        # given
        # when
        self.hash_table.add("test")
        # then
        self.assertEqual(self.hash_table.find("test"), "yes")
        self.assertEqual(self.hash_table.find("notfound"), "no")

    def test_should_delete(self):
        # given
        self.hash_table.add("test")
        # when
        self.hash_table.delete("test")
        # then
        self.assertEqual(self.hash_table.find("test"), "no")

    def test_should_check(self):
        # given
        # when
        self.hash_table.add("first")
        self.hash_table.add("second")
        self.hash_table.add("third")
        # then
        self.assertEqual(self.hash_table.check(0), "first")
        self.assertEqual(self.hash_table.check(1), "third")

    def test_should_multiple_collisions(self):
        # given
        strings = ["abc", "acb", "bac"]
        # when
        for s in strings:
            self.hash_table.add(s)
        # then
        for s in strings:
            self.assertEqual(self.hash_table.find(s), "yes")

    def test_should_check_out_of_bounds(self):
        self.assertEqual(self.hash_table.check(10), "")


if __name__ == "__main__":
    unittest.main()
