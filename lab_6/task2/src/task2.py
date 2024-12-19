from pathlib import Path
from lab_6.utils.utils import work
from lab_6.task1.src.task1 import HashTable


class PhoneBook(HashTable):
    def add_key(self, phone, user):
        self.table[phone] = user

    def find_number(self, phone):
        if phone in self.table.keys():
            return self.table[phone]
        return "not found"


def main(n, *actions):
    ans = []
    book = PhoneBook()
    for act in actions:
        print(act)
        match act[0]:
            case 'add':
                book.add_key(act[1], act[2])
            case 'del':
                book.del_key(act[1])
            case 'find':
                ans.append(book.find_number(act[1]))
    return ans


if __name__ == "__main__":
    work(Path(__file__), main)
