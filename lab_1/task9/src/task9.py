from pathlib import Path
from lab_1.utils.utils import work


def is_binary(a):
    return a == [int(elem) for elem in a]


def num_to_list(s):
    n = [int(ch) for ch in str(s)]
    return n


def binary_addition(a, b):
    a = num_to_list(a)
    b = num_to_list(b)
    n = len(a)
    if not (a and b and n == len(b) and n <= 10 ** 3):
        raise ValueError("Incorrect data")
    c = [0 for i in range(n + 1)]  # заполним список с нулями
    for i in range(n, 0, -1):  # начнем заполнять с конца
        c[i] = (c[i] + a[i - 1] + b[i - 1]) % 2
        c[i - 1] += (a[i - 1] + b[i - 1]) // 2
    return c


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, binary_addition)
