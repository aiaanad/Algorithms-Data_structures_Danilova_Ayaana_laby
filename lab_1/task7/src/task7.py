import pathlib
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.utils.utils import work


def sortland(n, arr):
    if not (1 <= n <= 10 ** 9 and len([x for x in arr if abs(x) <= 10 ** 9]) == n):
        raise ValueError("Incorrect data")
    id_numbers = [i + 1 for i in range(n)]
    for i in range(len(arr)):  # сортировка пузырьком
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                id_numbers[i], id_numbers[j] = id_numbers[j], id_numbers[i]
    return id_numbers[0], id_numbers[n // 2], id_numbers[-1]


if __name__ == "__main__":
    work(pathlib.Path(__file__).stem, sortland)

