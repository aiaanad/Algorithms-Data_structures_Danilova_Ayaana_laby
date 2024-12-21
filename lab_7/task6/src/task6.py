from pathlib import Path
from lab_6.utils.utils import work


def lis(n, arr):
    if not arr:
        return []

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    max_index = dp.index(max_length)

    result = [arr[max_index]]
    for i in range(max_index - 1, -1, -1):
        if arr[i] < arr[max_index] and dp[i] == max_length - 1:
            result.append(arr[i])
            max_length -= 1
            max_index = i

    return len(result), ' '.join(map(str, result[::-1]))


if __name__ == "__main__":
    work(Path(__file__), lis)



