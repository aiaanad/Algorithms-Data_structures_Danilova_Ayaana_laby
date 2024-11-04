from lab_3.utils import *
from lab_3.task1.src.task1 import partition3


def hirsh_index(a: list, l: int, r: int) -> int:
    res = []
    for i in range(r):
        k = i
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        if m1 <= r + 1 - a[m1]:
            res += [a[m1]]
    if len(res) == 0:
        return -1
    else:
        return max(res)


if __name__ == "__main__":
    work(hirsh_index, 0)
