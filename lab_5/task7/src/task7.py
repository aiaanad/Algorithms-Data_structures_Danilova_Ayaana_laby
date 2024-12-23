from lab_4.utils.utils import work
from pathlib import Path


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(arr, n, i):
    _l = left(i)
    r = right(i)

    if _l < n and arr[_l] > arr[i]:
        largest = _l
    else:
        largest = i

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_max_heap(arr, n):
    for i in range((len(arr) - 1) // 2, -1, -1):
        max_heapify(arr, n, i)


def heapsort(n, arr):
    build_max_heap(arr, n)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    work(Path(__file__), heapsort)
