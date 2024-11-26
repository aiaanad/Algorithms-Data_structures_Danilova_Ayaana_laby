import unittest
from lab_4.task13_2.src.task13_2 import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty_on_init(self):
        self.assertTrue(self.queue.isEmpty())

    def test_enqueue_and_is_empty(self):
        self.queue.enqueue(1)
        self.assertFalse(self.queue.isEmpty())

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue_empty_queue(self):
        result = self.queue.dequeue()
        self.assertIsNone(result)

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

    def test_repr(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(repr(self.queue), "1 2 ")

    def test_dequeue_until_empty(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertTrue(self.queue.isEmpty())


if __name__ == "__main__":
    unittest.main()