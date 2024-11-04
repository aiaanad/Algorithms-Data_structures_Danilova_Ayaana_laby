from lab_3.utils_for_tests import *
from lab_3.task7.src.task7 import radix_sort
import random

letters = []
letters += (chr(i) for i in range(ord('a'), ord('z') + 1))
min_args = (3, 3, 2, [[random.choice(letters) for j in range(3)] for i in range(3)])
min_time_memory(radix_sort, *min_args)

max_args = (10**2, 5*10**5, 10**5, [[random.choice(letters) for j in range(5*10**5)] for i in range(10**2)])
max_time_memory(radix_sort, *max_args)