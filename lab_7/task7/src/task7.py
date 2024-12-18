from pathlib import Path
import sys
from lab_7.utils.utils import work

sys.setrecursionlimit(10 ** 6)


def is_match(p, w, m, n, exist):
    key = (m, n)

    if m == len(p):
        exist[key] = (n == len(w))
        return m == len(w)

    if n == len(w):
        for x in p[m:]:
            if x is False:
                exist[key] = False
                return False
        exist[key] = True
        return True

    if p[m] == '?' or p[m] == w[n]:
        exist[key] = is_match(p, w, m + 1, n + 1, exist)
    elif p[m] == '*':
        exist[key] = is_match(p, w, m, n + 1, exist) or is_match(p, w, m + 1, n, exist)
    else:
        exist[key] = False

    return exist.get(key)


def main(pattern, word):
    exist = {}
    if is_match(pattern[0], word[0], 0, 0, exist):
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    work(Path(__file__), main)
