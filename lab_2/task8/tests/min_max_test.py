from lab_2.utils_for_tests import *
from lab_2.task8.src.task8 import *

min_args = (10,) + (random.sample(range(100), 10),) + (random.sample(range(100), 10),)
max_args = (10**3,) + (random.sample(range(10 ** 9), 10 ** 3),) + (random.sample(range(10 ** 9), 10 ** 3),)

min_time_memory(polynomial_mult, *min_args)
max_time_memory(polynomial_mult, *max_args)

