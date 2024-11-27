from lab_4.utils.utils import work
from pathlib import Path
from collections import deque


class Stack:
    def __init__(self):
        self.stack_ = deque()

    def push(self, item):
        if self.stack_:
            new_max = max(item, self.stack_[-1][1])
        else:
            new_max = item
        self.stack_.append((item, new_max))

    def pop(self):
        if self.stack_:
            return self.stack_.pop()[0]

    def get_max(self):
        if self.stack_:
            return self.stack_[-1][1]


def main(n, *operations):
    my_queue = Stack()
    max_values = []
    for f in operations:
        if f[0] == 'push':
            my_queue.push(f[1])
        elif f[0] == 'pop':
            my_queue.pop()
        elif f[0] == 'max':
            max_values.append(my_queue.get_max())
    return max_values


if __name__ == "__main__":
    work(Path(__file__), main)
