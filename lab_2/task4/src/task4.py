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


'''
file = open('input.txt', 'r')
n1 = int(file.readline())
data1 = [int(elem) for elem in file.readline().split() if 1 <= int(elem) <= 10e9]
n2 = int(file.readline())
data2 = [int(elem) for elem in file.readline().split() if 1 <= int(elem) <= 10e9]
file.close()
with open('output.txt', 'w') as ans:
    if not 1 <= min(n1, n2) <= max(n1, n2) <= 10e3 and (n1 == len(data1) and n2 == len(data2)):
        ans.write('---Incorrect data---')
    else:
        ans.write(' '.join(map(str, binary_search(n1, data1, n2, data2))))
'''