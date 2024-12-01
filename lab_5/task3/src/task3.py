from lab_5.utils.utils import work
from pathlib import Path


def processing_net_packets(s: int, n: int, *packages):
    if n == 0:
        return None
    deque = []
    result = []
    head = 0
    buffer_time = packages[0][0]
    for p in packages:
        start_time, p_i = p
        head = max([head] + [index for index in range(len(deque)) if deque[index] <= start_time])
        if len(deque[head+1:]) < s:
            result += [max(buffer_time, start_time)]
            buffer_time += p_i
            deque.append(buffer_time)
        else:
            result += [-1]
    return result


if __name__ == "__main__":
    work(Path(__file__), processing_net_packets)