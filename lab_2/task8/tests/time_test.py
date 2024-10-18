import time
from lab_2.task8.src.task8 import polynomial_mult
import random


def max_input():

    a = random.sample(range(10 ** 9), 1000)
    b = random.sample(range(10 ** 9), 1000)

    start = time.perf_counter()
    polynomial_mult(1000, a, b)
    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    # print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")


def min_input():
    a = random.sample(range(10), 5)
    b = random.sample(range(10), 5)
    start = time.perf_counter()
    polynomial_mult(1000, a, b)
    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    # print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")


min_input()
print()
max_input()
print()