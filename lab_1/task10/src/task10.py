from pathlib import Path
from lab_1.utils.utils import work


def palindrome(n, word):
    word = sorted(word)
    mid = 'a'

    for i in range(n):
        if word.count(word[i]) % 2 != 0 and word[i] < mid:
            mid = word[i]
            break
        mid = ''  # средний элемент

    right = []  # правая часть ответа
    left = []  # левая
    for elem in word:
        count = left.count(elem) + right.count(elem)  # количество в правой и левой части
        if count % 2 == 0 and word.count(elem) - count > 1:
            left.append(elem)
        elif count % 2 != 0:
            right.append(elem)
    return ''.join(left) + mid + ''.join(right[::-1])


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, palindrome)
