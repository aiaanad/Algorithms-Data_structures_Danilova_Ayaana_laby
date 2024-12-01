from lab_5.utils.utils import work
from pathlib import Path


def left_child_idx(i):
    return 2 * i + 1


def right_child_idx(i):
    return 2 * i + 2


def is_heap(n, arr):
    for i in range(len(arr) // 2):
        if arr[i] > arr[left_child_idx(i)]:
            return "NO"
        if right_child_idx(i) < len(arr) and arr[i] > arr[right_child_idx(i)]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    work(Path(__file__), is_heap)
