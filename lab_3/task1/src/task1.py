import random
from pathlib import Path
from lab_3.utils.utils import work


def partition(a: list, l: int, r: int) -> int:
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def partition3(a: list, l: int, r: int) -> tuple:
    x = a[l]
    m1 = l
    m2 = r
    i = l

    while i <= m2 and m1 <= m2:
        if a[i] < x:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1
        elif a[i] > x:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        elif a[i] == x:
            i += 1
    return m1, m2


def randomized_quicksort(a: list, l: int, r: int) -> list:
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        randomized_quicksort(a, l, m1 - 1)
        randomized_quicksort(a, m2 + 1, r)
    return a


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, randomized_quicksort, 0)
