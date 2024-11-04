from lab_3.utils.utils import *


def is_correct(a: list) -> bool:
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


def bugaboo(n: int, k: int, a: list) -> str:
    for i in range(n - k):
        if a[i] > a[i + k]:
            a[i], a[i + k] = a[i + k], a[i]
    if is_correct(a):
        return "ДА"
    else:
        return "НЕТ"


if __name__ == "__main__":
    work(bugaboo)
