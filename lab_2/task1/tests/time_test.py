import time
from lab_2.task1.task1 import mergeSort


def max_input():

    input_data = [(10**9 - i) for i in range(10**5)]
    start = time.perf_counter()
    mergeSort(input_data, 0, 10**5 - 1)
    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    # print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")


def min_input():
    input_data = [(10**9 - 10**5 + i + 1) for i in range(10**5)]
    start = time.perf_counter()
    mergeSort(input_data, 0, 10 ** 5 - 1)
    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    # print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")


min_input()
print()
max_input()
print()