import random
import time
from lab_2.task5.task5 import majority


def max_input():

    input_data = random.sample(range(10 ** 9), 10 ** 5)
    start = time.time()
    majority(len(input_data), input_data)
    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.time() - start))


def min_input():

    input_data = random.sample(range(10), 1)
    start = time.perf_counter()
    majority(len(input_data), input_data)
    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))


min_input()
print()
max_input()
print()



