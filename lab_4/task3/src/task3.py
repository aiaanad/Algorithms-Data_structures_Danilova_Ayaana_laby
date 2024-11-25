from collections import deque
from pathlib import Path
from lab_4.utils.utils import work


def isValid(s: str) -> bool:
    stack = deque()
    parenth = {
        "(": ")",
        "[": "]"
    }
    for br in s:
        if br in parenth:
            stack.append(br)
        else:
            if stack and parenth[stack.pop()] == br:
                continue
            else:
                return False
    return not stack


def bracket_sequence(n, *data):
    ans = []
    ans += ["YES" if isValid(sequence[0]) else "NO" for sequence in data]
    return ans


if __name__ == "__main__":
    work(Path(__file__), bracket_sequence)
