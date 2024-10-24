from lab_2.task1.tests.utils2 import *
from lab_2.task1.src.task1 import mergeSort

min_args = ([(10e9 - 10e5 + i + 1) for i in range(10**3)],) + (0,) + (10**3-1,)
max_args = ([(10e9 - i) for i in range(10**5)],) + (0,) + (10**5-1,)

min_time_memory(mergeSort, *min_args)
max_time_memory(mergeSort, *max_args)
