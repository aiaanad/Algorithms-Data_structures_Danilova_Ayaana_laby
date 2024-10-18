import tracemalloc
from lab_2.task1.src.task1 import mergeSort


def max_input():

    input_data = [(10e9 - i) for i in range(100000)]
    tracemalloc.start()
    mergeSort(input_data, 0, 10**5 - 1)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    input_data = [(10e9 - 10e5 + i + 1) for i in range(1000)]
    tracemalloc.start()
    mergeSort(input_data, 0, 999)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()