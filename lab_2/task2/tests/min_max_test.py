from lab_2.utils.utils_for_tests import *
from lab_2.task2.src.task2 import mergeSort
import random

min_args = (random.sample(range(100), 10),) + (0,) + (9,)
max_args = (random.sample(range(10 ** 9), 10 ** 5),) + (0,) + (10**5-1,)

min_time_memory(mergeSort, *min_args)
max_time_memory(mergeSort, *max_args)