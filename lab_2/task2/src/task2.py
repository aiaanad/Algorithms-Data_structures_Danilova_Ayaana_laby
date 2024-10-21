from lab_2.task1.src.utils import f_read, f_write, check


def merge(arr, left, m, right):
    n1 = m - left + 1
    n2 = right - m

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
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    coordinates = str(left + 1) + ' ' + str(right + 1) + ' ' + str(arr[left]) + ' ' + str(arr[right]) + '\n'
    f_write(coordinates)


def mergeSort(arr, left, right):
    if left < right:
        m = (left + right) // 2

        mergeSort(arr, left, m)
        mergeSort(arr, m + 1, right)
        merge(arr, left, m, right)

        return arr


if __name__ == "__main__":
    n, array = f_read()
    if check(n, array):
        result = mergeSort(array, 0, n - 1)
        f_write(result)
    else:
        f_write('---Incorrect data---')
