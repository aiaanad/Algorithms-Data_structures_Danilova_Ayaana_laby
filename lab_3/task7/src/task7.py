from lab_3.utils.utils import *


def radix_sort(n: int, m: int, k: int, a: list) -> list:
    original = a
    alpha = 26
    for i in range(m - 1, m - k - 1, -1):
        res = [''] * n
        c = [0] * alpha

        for j in range(n):
            d = ord(a[j][i]) - ord('a')
            c[d] += 1

        count = 0
        for j in range(alpha):
            tmp = c[j]
            c[j] = count
            count += tmp

        for j in range(n):
            d = ord(a[j][i]) - ord('a')
            res[c[d]] = a[j]
            c[d] += 1
        a = res
    ans = [original.index(a[i]) + 1 for i in range(len(a))]
    return ans


if __name__ == "__main__":
    work(radix_sort)
