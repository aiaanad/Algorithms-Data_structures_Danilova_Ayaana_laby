from pathlib import Path
from lab_1.utils.utils import work


def radix_sort(nmk: list, *a) -> list:
    n, m, k = nmk[0], nmk[1], nmk[2]
    original = list(a)
    print(original)
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
    work(Path(__file__).parts[-4], Path(__file__).stem, radix_sort)
