import random
import tracemalloc
from lab_2.task8.src.task8 import polynomial_mult


def max_input():

    a = random.sample(range(10 ** 9), 1000)
    b = random.sample(range(10 ** 9), 1000)
    tracemalloc.start()
    polynomial_mult(1000, a, b)
    print('Для максимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():

    a = random.sample(range(100), 10)
    b = random.sample(range(100), 10)
    tracemalloc.start()
    polynomial_mult(10, a, b)
    print('Для минимальных значений:')
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
print()
