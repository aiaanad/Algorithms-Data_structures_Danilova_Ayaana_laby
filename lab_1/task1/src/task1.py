from pathlib import Path
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.utils.utils import work


def insertion_sort(n, arr):
    if not(1 <= n <= 10**9 and len([x for x in arr if abs(x) <= 10**9]) == n):
        raise ValueError("Incorrect data")
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, insertion_sort)
