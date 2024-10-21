from lab_2.task1.src.task1 import mergeSort
from lab_2.task1.src.utils import f_read, f_write, check


def majority(n, array):
    mergeSort(array, 0, n - 1)
    mid = (0 + n) // 2
    first_entry = array.index(array[mid])
    last_entry = n - array[::-1].index(array[mid]) - 1
    if last_entry - first_entry >= mid:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n, array = f_read()
    if check(n, array):
        f_write(majority(n, array))
    else:
        f_write('---Incorrect data---')
