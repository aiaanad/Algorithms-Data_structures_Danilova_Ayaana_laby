from pathlib import Path
from lab_3.utils.utils import work


def qsort(a: list, left: int, right: int) -> list:
    key = a[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:
            i += 1
        while a[j] > key:
            j -= 1
        if i <= j:
            if a[i] != a[j]:
                print(a, 1, end=' ')
            a[i], a[j] = a[j], a[i]
            print(a)
            i += 1
            j -= 1

        if left < j:
            qsort(a, left, j)
        if i < right:
            qsort(a, i, right)
        return a


def anti_qsort(n: int) -> list:
    a = [i + 1 for i in range(n)]
    for i in range(2, len(a)):
        a[i], a[i // 2] = a[i // 2], a[i]
    return a


if __name__ == "__main__":
    work(Path(__file__).stem, anti_qsort)
