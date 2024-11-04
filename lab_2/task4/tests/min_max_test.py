from lab_2.utils.utils_for_tests import *
from lab_2.task4.src.task4 import *

min_args = (10,) + (random.sample(range(100), 10),) + (10,) + (random.sample(range(100), 10),)
max_args = (10**5,) + (random.sample(range(10 ** 9), 10 ** 5),) + (10**5,) + (random.sample(range(10 ** 9), 10 ** 5),)

min_time_memory(binary_search, *min_args)
max_time_memory(binary_search, *max_args)

