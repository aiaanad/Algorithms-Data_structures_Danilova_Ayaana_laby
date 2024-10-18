from lab_2.task1.task1 import mergeSort


def majority(n, array):

    mergeSort(array, 0, n - 1)
    mid = (0 + n) // 2
    first_entry = array.index(array[mid])
    last_entry = n - array[::-1].index(array[mid]) - 1
    if last_entry - first_entry >= mid:
        return 1
    else:
        return 0


'''
file = open('input.txt', 'r')
n = int(file.readline())
array = [int(elem) for elem in file.readline().split() if 1 <= int(elem) <= 10e9]
file.close()
with open('output.txt', 'w') as ans:
    if not (1 <= n <= 10e5 and len(array) == n):
        ans.write('---Incorrect data---')
    else:
        ans.write(str(majority(n, array)))
'''