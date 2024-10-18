def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
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


def mergeSort(arr, l, r):
    if l < r:

        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

    return arr


'''
file = open('input.txt', 'r')
n = int(file.readline())
data = [int(elem) for elem in file.readline().split() if abs(int(elem)) <= 10e9]
file.close()
with open('output.txt', 'w') as ans:
    if not (1 <= n <= 10e3 and n == len(data)):
        ans.write('---Incorrect data---')
    else:
        ans.write(' '.join(map(str, mergeSort(data, 0, n - 1))))
'''


