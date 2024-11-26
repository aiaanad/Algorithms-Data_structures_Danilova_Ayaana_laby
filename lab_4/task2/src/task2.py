from pathlib import Path
from lab_4.utils.utils import work
from collections import deque


def realize_queue(n: int, *operations) -> list:
    my_queue = deque()
    deleted = []
    for f in operations:
        if len(f) == 2:
            my_queue.append(f[1])
        else:
            deleted.append(my_queue.popleft())
    print(my_queue)
    return deleted


if __name__ == "__main__":
    work(Path(__file__), realize_queue)
