from lab_4.utils.utils import work
from pathlib import Path


class InLine:
    def __init__(self):
        self.left = 0
        self.right = 0


class Formation:
    def __init__(self, n):
        self.a = [InLine() for _ in range(n + 1)]

    def go_left(self, i, j):
        self.a[i].left = self.a[j].left
        if self.a[i].left != 0:
            self.a[self.a[i].left].right = i
        self.a[j].left = i
        self.a[i].right = j

    def go_right(self, i, j):
        self.a[i].right = self.a[j].right
        if self.a[i].right != 0:
            self.a[self.a[i].right].left = i
        self.a[j].right = i
        self.a[i].left = j

    def go_out(self, i):
        if self.a[i].left != 0:
            self.a[self.a[i].left].right = self.a[i].right
        if self.a[i].right != 0:
            self.a[self.a[i].right].left = self.a[i].left
        self.a[i].left = 0
        self.a[i].right = 0

    def tell_neighbours(self, i):
        return f"{self.a[i].left} {self.a[i].right}"


def main(n, m, *operations):
    formation = Formation(n)
    ans = []
    for action in operations:
        if action[0] == "left":
            i, j = int(action[1]), int(action[2])
            formation.go_left(i, j)
        elif action[0] == "right":
            i, j = int(action[1]), int(action[2])
            formation.go_right(i, j)
        elif action[0] == "leave":
            i = int(action[1])
            formation.go_out(i)
        elif action[0] == "name":
            i = int(action[1])
            ans += [formation.tell_neighbours(i)]

    return ans


if __name__ == "__main__":
    work(Path(__file__), main)
