import pathlib
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.utils.utils import work


def insertion_sort_plus(n, arr):
    if not (1 <= n <= 10 ** 9 and len([x for x in arr if abs(x) <= 10 ** 9]) == n):
        raise ValueError("Incorrect list array")
    new_index = [1]  # создаем список новых индексов
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        new_index.append(i + 2)
    return new_index


if __name__ == "__main__":
    work(pathlib.Path(__file__).stem, insertion_sort_plus)