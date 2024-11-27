import unittest
from lab_4.task13_1.src.task13_1 import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty_on_init(self):
        self.assertTrue(self.stack.isEmpty())

    def test_push_and_is_empty(self):
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_push_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertFalse(self.stack.isEmpty())

    def test_pop_single_element(self):
        self.stack.push(1)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.isEmpty())

    def test_pop_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 3)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 2)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.isEmpty())

    def test_pop_empty_stack(self):
        result = self.stack.pop()
        self.assertIsNone(result)

    def test_printstack_empty(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.stack.printstack()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), 'List is Empty')

    def test_printstack_non_empty(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.stack.push(1)
        self.stack.push(2)
        self.stack.printstack()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), 'Stack is :  1 2')


if __name__ == "__main__":
    unittest.main()