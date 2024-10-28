from lab_2.utils import *


def merge(arr, left, m, r):
    global local_var
    n1 = m - left + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] > R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            local_var += i
            # print(i, arr)
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        local_var += i
        # print(i, arr)
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        m = (left + right) // 2

        mergeSort(arr, left, m)
        mergeSort(arr, m + 1, right)
        merge(arr, left, m, right)

    return arr


def inversion_number(lenarr, arr):
    global local_var
    local_var = 0
    mergeSort(arr, 0, lenarr - 1)

    return local_var


if __name__ == "__main__":
    work(inversion_number)
