import random
import tracemalloc
from lab_2.task5.src.task5 import majority


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    tracemalloc.start()
    majority(len(input_data), input_data)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    tracemalloc.start()
    majority(len(input_data), input_data)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()
