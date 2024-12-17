import time
import unittest
import random
import tracemalloc
from lab_6.task1.src.task1 import main, HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_should_add_key(self):
        # given
        # when
        self.ht.add_key("key1")
        # then
        self.assertTrue(self.ht.key_in_table("key1"))

    def test_should_add_duplicate_key(self):
        # given
        # when
        self.ht.add_key("key1")
        self.ht.add_key("key1")
        # then
        self.assertEqual(len(self.ht.table), 1)

    def test_should_del_key(self):
        # given
        self.ht.add_key("key1")
        # when
        self.ht.del_key("key1")
        # then
        self.assertFalse(self.ht.key_in_table("key1"))

    def test_should_del_nonexistent_key(self):
        self.ht.del_key("nonexistent")

    def test_should_key_in_table(self):
        self.assertFalse(self.ht.key_in_table("key2"))
        self.ht.add_key("key2")
        self.assertTrue(self.ht.key_in_table("key2"))

    def test_should_ht_with_max_args(self):
        # given
        args = (5 * 10 ** 4,)
        expected_result = []
        expected_time = 2
        expected_memory = 256

        arr = []
        for i in range(args[0]):
            act = random.choice(['A', 'D', '?'])
            val = random.randint(1, 10 ** 9)
            args += ([act, val],)
            match act:
                case 'A':
                    arr.append(val)
                case 'D':
                    if val in arr:
                        arr.pop(arr.index(val))
                case '?':
                    expected_result += 'Y\n' if val in arr else 'N\n'

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
