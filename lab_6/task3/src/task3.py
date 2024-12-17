from pathlib import Path
from lab_6.utils.utils import work
from collections import deque


class HashTableChaining:
    def __init__(self, m):
        self.m = m
        self.p = 1000000007
        self.x = 263
        self.table = [deque() for _ in range(m)]
        self.exist = set()

    def hash_func(self, s):
        h = 0
        for i in range(len(s)):
            h += ord(s[i]) * self.x ** i
        return (h % self.p) % self.m

    def add(self, s):
        if s in self.exist:
            return
        self.exist.add(s)
        key = self.hash_func(s)
        self.table[key].appendleft(s)

    def delete(self, s):
        if s not in self.exist:
            return
        self.exist.remove(s)
        index = self.hash_func(s)
        self.table[index].remove(s)

    def find(self, s):
        return 'yes' if s in self.exist else 'no'

    def check(self, i):
        if 0 <= i < self.m:
            return ' '.join(self.table[i])
        return ''


def main(m, n, *actions):
    arr = HashTableChaining(m)
    ans = []
    for act, arg in actions:
        match act:
            case 'add':
                arr.add(arg)
            case 'del':
                arr.delete(arg)
            case 'find':
                ans.append(arr.find(arg))
            case 'check':
                ans.append(arr.check(arg))
    return ans


if __name__ == "__main__":
    work(Path(__file__), main)
    a = HashTableChaining(5)
    print(a.hash_func('third'))
