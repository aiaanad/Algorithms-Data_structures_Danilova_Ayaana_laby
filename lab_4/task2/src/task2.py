from ...utils.utils import work
from collections import deque
from pathlib import Path
from pprint import pprint
import sys


def realize_queue(m: int, *operations) -> list:
    my_queue = deque()
    deleted = []
    for f in operations:
        if len(f) == 2:
            my_queue.append(f[1])
        elif len(my_queue) > 0:
            deleted.append(my_queue.popleft())
    return deleted


if __name__ == "__main__":
    pprint(sys.path)
    work(Path(__file__).stem, realize_queue)
