from lab_3.utils.utils_for_tests import *
from lab_3.task8.src.task8 import nearest_point
import random


min_args = (1, 1, [3, 4])
min_time_memory(nearest_point, *min_args)

max_args = (10**5, 99999, [random.sample(range(-10**9, 10**9), 2) for i in range(10**5)])
max_time_memory(nearest_point, *max_args)