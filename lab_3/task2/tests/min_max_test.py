from lab_3.utils.utils_for_tests import *
from lab_3.task2.src.task2 import anti_qsort

min_args = (3,)
max_args = (10**5,)

min_time_memory(anti_qsort, *min_args)
max_time_memory(anti_qsort, *max_args)