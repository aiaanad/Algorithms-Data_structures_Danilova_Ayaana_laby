from pathlib import Path
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from lab_1.utils.utils import work


def palindrom(n, word):
    for i in range(n):  # сортировка пузырьком
        for j in range(i + 1, len(word)):
            if word[j] < word[i]:
                word[i], word[j] = word[j], word[i]

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
        if count % 2 == 0:
            if word.count(elem) - count > 1:
                left.append(elem)
        else:
            right.append(elem)
    return ''.join(left) + mid + ''.join(right[::-1])


if __name__ == "__main__":
    work(Path(__file__).parts[-4], Path(__file__).stem, palindrom)
