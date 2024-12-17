import unittest
from lab_6.task2.src.task2 import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.pb = PhoneBook()

    def test_should_add_number(self):
        # given
        # when
        self.pb.add_key("1234567890", "Alice")
        # then
        self.assertEqual(self.pb.find_number("1234567890"), "Alice")

    def test_should_del_number(self):
        # given
        self.pb.add_key("1234567890", "Alice")
        # then
        self.pb.del_key("1234567890")
        # when
        self.assertEqual(self.pb.find_number("1234567890"), "not found")

    def test_should_find_nonexistent_number(self):
        self.assertEqual(self.pb.find_number("0987654321"), "not found")

    def test_should_add_duplicate_number(self):
        # given
        # when
        self.pb.add_key("1234567890", "Alice")
        self.pb.add_key("1234567890", "Bob")
        # then
        self.assertEqual(self.pb.find_number("1234567890"), "Bob")


if __name__ == "__main__":
    unittest.main()
