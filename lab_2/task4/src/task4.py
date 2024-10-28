from lab_2.utils import *


def binary_search(len1: int, search_in: list, len2: int, the_search: list):

    answer = [-1] * len2
    for i in range(len2):
        low = 0
        high = len1 - 1

        while low <= high:

            mid = (high + low) // 2

            if search_in[mid] < the_search[i]:
                low = mid + 1
            elif search_in[mid] > the_search[i]:
                high = mid - 1
            else:
                answer[i] = mid
                break

    return answer


if __name__ == "__main__":
    work(binary_search)
