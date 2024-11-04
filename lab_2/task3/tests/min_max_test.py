from lab_2.utils.utils_for_tests import *
from lab_2.task3.src.task3 import *

min_args = (10,) + (random.sample(range(100), 10),)
max_args = (10**5,) + (random.sample(range(10 ** 9), 10 ** 5),)

min_time_memory(inversion_number, *min_args)
max_time_memory(inversion_number, *max_args)

