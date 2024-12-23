from pathlib import Path
from lab_1.utils.utils import work
from lab_3.task1.src.task1 import partition3


def hirsh_index(a: list, l, r) -> int:
    res = []

    for i in range(r + 1):
        k = i
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        print(m1, a[m1], m2, a[m2])
        if m1 <= a[m1] <= (r - m1 + 1):
            res += [a[m1]]
    if len(res) == 0:
        return -1
    else:
        return max(res)


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, hirsh_index, 0)
