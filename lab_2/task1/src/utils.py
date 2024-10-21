def f_read():
    file = open('../txtf/input.txt', 'r')
    n = int(file.readline())
    array = [int(elem) for elem in file.readline().split()]
    file.close()
    return n, array


def f_read_2():
    file = open('../txtf/input.txt', 'r')
    n1 = int(file.readline())
    array1 = [int(elem) for elem in file.readline().split()]
    n2 = int(file.readline())
    array2 = [int(elem) for elem in file.readline().split()]
    file.close()
    return n1, array1, n2, array2


def f_read_3():
    file = open('../txtf/input.txt', 'r')
    n = int(file.readline())
    array1 = [int(elem) for elem in file.readline().split()]
    array2 = [int(elem) for elem in file.readline().split()]
    file.close()
    return n, array1, array2


def check(n, array):
    if 1 <= n <= 10e5 and max(array) <= 10e9 and min(array) >= -10e9:
        return True
    else:
        return False


def f_write(answer):
    with open('../txtf/output.txt', 'a') as file:
        if type(answer) == list:
            answer = ' '.join(map(str, answer)) + '\n'
        elif type(answer) == int:
            answer = str(answer)
        file.write(answer)
