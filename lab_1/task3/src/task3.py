from pathlib import Path
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.utils.utils import work


def swap(a, b):
    return b, a


def insertion_sort_r(n, arr):
    if not (1 <= n <= 10 ** 9 and len([x for x in arr if abs(x) <= 10 ** 9]) == n):
        raise ValueError("Incorrect data")
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:  # направление знака меняется
            arr[i + 1], arr[i] = swap(arr[i + 1], arr[i])
            i = i - 1
    return arr


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, insertion_sort_r)


'''
    Да, алгоритм сортировки вставками можно написать с помощью рекурсии на Python.
    Идея реализации:
        Базовый случай: если размер массива равен 1 или меньше, вернуть значение.
        Рекурсивно отсортировать первые n-1 элементов. 
        Вставить последний элемент на правильную позицию в отсортированном массиве.
'''