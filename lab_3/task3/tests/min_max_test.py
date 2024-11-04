from lab_3.utils.utils_for_tests import *
from lab_3.task3.src.task3 import bugaboo
import random

min_args = (3, 2) + (random.sample(range(10), 3),)
max_args = (10**5, 1) + (random.sample(range(10**9), 10**5),)

min_time_memory(bugaboo, *min_args)
max_time_memory(bugaboo, *max_args)