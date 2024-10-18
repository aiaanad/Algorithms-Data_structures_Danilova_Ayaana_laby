import random
import tracemalloc
from lab_2.task3.src.task3 import inversion_number


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    tracemalloc.start()
    inversion_number(len(input_data), input_data)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    input_data = random.sample(range(100), 10)
    tracemalloc.start()
    inversion_number(len(input_data), input_data)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()
