import random
import time
from lab_2.task2.src.task2 import mergeSort


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    start = time.perf_counter()
    mergeSort(input_data, 0, 10**5 - 1)
    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))


def min_input():

    input_data = random.sample(range(100), 10)
    start = time.perf_counter()
    mergeSort(input_data, 0, 9)
    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))


min_input()
print()
max_input()
print()

