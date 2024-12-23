from pathlib import Path
from collections import OrderedDict
from lab_4.utils.utils import work


def main(*actions):
    a = OrderedDict()
    for candidate, votes in actions:
        if candidate not in a:
            a[candidate] = int(votes)
        else:
            a[candidate] += int(votes)
    a = OrderedDict(sorted(a.items()))
    ans = [f'{pair[0]} {pair[1]}' for pair in list(a.items())]
    return ans


if __name__ == "__main__":
    work(Path(__file__), main)
