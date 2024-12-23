from math import ceil, log
from pathlib import Path
from lab_1.utils.utils import work


def binary(lenarr, array):
    # добавление нулей для: n = степень двойки
    return [0] * (2 ** ceil(log(lenarr, 2)) - lenarr) + array


def mult2(a, b, n, al, bl):
    r = [0] * (2 * n - 1)
    if n == 1:
        r[0] = a[al] * b[bl]
        return r

    r[0: n - 1] = mult2(a, b, n // 2, al, bl)
    r[n: 2 * n - 1] = mult2(a, b, n // 2, (al + n // 2), (bl + n // 2))

    de = mult2(a, b, n // 2, al, (bl + (n // 2)))
    ed = mult2(a, b, n // 2, (al + (n // 2)), bl)

    k = 0
    for i in range(n // 2, n + n // 2 - 1):
        r[i] += de[k] + ed[k]
        k += 1
        if k >= len(de):
            break

    return r


def polynomial_mult(n, a, b):
    real_n = n
    a = binary(n, a)
    b = binary(n, b)
    n = len(a)
    al, bl = 0, 0
    answer = mult2(a, b, n, al, bl)

    return answer[len(answer) - 2 * real_n + 1:]


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, polynomial_mult)
