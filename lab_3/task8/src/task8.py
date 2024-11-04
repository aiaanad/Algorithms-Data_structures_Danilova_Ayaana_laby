import random
from math import *
from lab_3.utils.utils import *


def distance(t: list) -> float:
    x = t[0]
    y = t[1]
    return sqrt(x**2 + y**2)


def partition3(a: list, l: int, r: int) -> tuple:
    x = a[l]
    m1 = l
    m2 = r
    i = l

    while i <= m2 and m1 <= m2:
        if distance(a[i]) < distance(x):
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1
        elif distance(a[i]) > distance(x):
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        elif distance(a[i]) == distance(x):
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


def nearest_point(n: int, k: int, a: list) -> list:
    a = randomized_quicksort(a, 0, n - 1)
    return a[:k]


if __name__ == "__main__":
    work(nearest_point)

