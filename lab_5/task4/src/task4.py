from lab_5.utils.utils import work
from pathlib import Path


class MinHeap:
    def __init__(self, n, array):
        self.heap = array
        self.high = n
        self.swaps = []

    def heap_sort(self):
        for i in range(self.high // 2 - 1, -1, -1):
            self.swap(i)
        return len(self.swaps), self.swaps

    def swap(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.high and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.high and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swaps += [(index, smallest)]
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.swap(smallest)


def main(n, arr):
    return MinHeap(n, arr).heap_sort()


if __name__ == "__main__":
    work(Path(__file__), main)