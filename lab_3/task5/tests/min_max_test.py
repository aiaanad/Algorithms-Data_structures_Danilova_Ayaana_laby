from lab_3.utils_for_tests import *
from lab_3.task5.src.task5 import hirsh_index
import random

min_args = (random.sample(range(10), 3), 0, 2)
max_args = (random.sample(range(10**9), 10**4), 0, 9999)

min_time_memory(hirsh_index, *min_args)
max_time_memory(hirsh_index, *max_args)