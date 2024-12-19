from pathlib import Path
from collections import defaultdict
from lab_7.utils.utils import work


def simple_calculator(n):
    if n == 1:
        return 0, 1
    md = defaultdict(list)
    md[1] = [1]
    md[2] = [1, 2]
    md[3] = [1, 3]
    for i in range(4, n + 1):
        if i not in md:
            md[i] = md[i - 1] + [i]
            if i % 6 == 0:
                md[i] = sorted([md[i // 3] + [i], md[i // 2] + [i], md[i]], key=len)[0]
            elif i % 3 == 0:
                md[i] = sorted([md[i // 3] + [i], md[i]], key=len)[0]
            elif i % 2 == 0:
                md[i] = sorted([md[i // 2] + [i], md[i]], key=len)[0]
    return len(md[n]) - 1, ' '.join(map(str, md[n]))


if __name__ == "__main__":
    work(Path(__file__), simple_calculator)

