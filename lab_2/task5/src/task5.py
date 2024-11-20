from pathlib import Path
from lab_2.utils.utils import work
from lab_2.task1.src.task1 import mergeSort


def majority(n, array):
    array = mergeSort(array, 0, n - 1)
    mid = (0 + n) // 2
    first_entry = array.index(array[mid])
    last_entry = n - array[::-1].index(array[mid]) - 1
    if last_entry - first_entry >= mid:
        return 1
    else:
        return 0


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, majority)
