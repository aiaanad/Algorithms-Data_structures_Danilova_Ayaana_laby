from lab_3.utils.utils_for_tests import *
from lab_3.task1.src.task1 import randomized_quicksort
import random

min_args = (random.sample(range(100), 10),) + (0,) + (9,)
max_args = (random.sample(range(10 ** 9), 10 ** 5),) + (0,) + (10**5-1,)

min_time_memory(randomized_quicksort, *min_args)
max_time_memory(randomized_quicksort, *max_args)