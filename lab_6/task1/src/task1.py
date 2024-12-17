from pathlib import Path
from lab_6.utils.utils import work


class HashTable:
    def __init__(self):
        self.table = {}

    def key_in_table(self, key):
        if key in self.table:
            return True
        return False

    def add_key(self, key, val=None):
        if not self.key_in_table(key):
            self.table[key] = val

    def del_key(self, key):
        if self.key_in_table(key):
            self.table.pop(key)


def main(n, *actions):
    ans = []
    arr = HashTable()
    for act, key in actions:
        match act:
            case 'A':
                arr.add_key(key)
            case 'D':
                arr.del_key(key)
            case '?':
                ans += 'Y' if arr.key_in_table(key) else 'N'
    return ans


if __name__ == "__main__":
    work(Path(__file__), main)



