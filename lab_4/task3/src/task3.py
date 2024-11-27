from collections import deque
from pathlib import Path
from lab_4.utils.utils import work


def isValid(s: str) -> bool:
    stack = deque()
    brackets = {
        "(": ")",
        "[": "]"
    }
    for br in s:
        if br in brackets:
            stack.append(br)
        else:
            if stack and brackets[stack.pop()] == br:
                continue
            else:
                return False
    return not stack


def bracket_sequence(n, *data):
    ans = []
    for seq in data:
        if isValid(seq[0]):
            ans.append('YES')
        else:
            ans.append('NO')
    return ans


if __name__ == "__main__":
    work(Path(__file__), bracket_sequence)
