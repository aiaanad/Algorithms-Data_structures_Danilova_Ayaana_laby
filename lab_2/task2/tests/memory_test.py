import random
import tracemalloc
from lab_2.task2.src.task2 import mergeSort


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    tracemalloc.start()
    mergeSort(input_data, 0, 10**5 - 1)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    input_data = random.sample(range(100), 10)
    tracemalloc.start()
    mergeSort(input_data, 0, 9)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()