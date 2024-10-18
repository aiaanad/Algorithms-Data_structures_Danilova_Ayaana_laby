import random
import time
from lab_2.task3.src.task3 import inversion_number


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    start = time.perf_counter()
    inversion_number(len(input_data), input_data)
    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))

def min_input():

    input_data = random.sample(range(100), 10)
    start = time.perf_counter()
    inversion_number(len(input_data), input_data)
    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))


min_input()
print()
max_input()
print()

