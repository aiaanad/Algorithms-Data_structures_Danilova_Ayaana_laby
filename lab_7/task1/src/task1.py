from pathlib import Path
from collections import defaultdict
from lab_6.utils.utils import work


def coin_exchange(money, k, coins):
    mcn = defaultdict(int)
    for coin in coins:
        mcn[coin] = 1
    for i in range(min(coins), money + 1):
        if i not in mcn:
            mcn[i] = 10 ** 9
            for coin in coins:
                if coin < i:
                    mcn[i] = min(mcn[i], mcn[i - coin] + 1)
    return mcn[money]


def coin_exchange_2(money, k, coins, counts):
    mcn = defaultdict(int)
    for coin in coins:
        mcn[coin] = 1
    for i in range(min(coins), money + 1):
        if i not in mcn:
            mcn[i] = 10 ** 9
            free = counts
            for coin in coins:
                if coin < i and free[coin - 1] > 0:
                    mcn[i] = min(mcn[i], mcn[i - coin] + 1)
    return mcn[money]


if __name__ == "__main__":
    work(Path(__file__), coin_exchange)

