import random
import tracemalloc
from lab_2.task4.task4 import binary_search


def max_input():

    the_search = random.sample(range(10 ** 9), 10 ** 5)
    search_in = random.sample(range(10 ** 9), 10 ** 5)
    tracemalloc.start()
    binary_search(len(the_search), the_search, len(search_in), search_in)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    the_search = random.sample(range(100), 10)
    search_in = random.sample(range(100), 10)
    tracemalloc.start()
    binary_search(len(the_search), the_search, len(search_in), search_in)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()

