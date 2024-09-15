def first_1():
    a, b = map(int, input().split())
    ans = a + b
    print(ans)
def first_2():
    a, b = map(int, input().split())
    ans = a ** 2 + b
    print(ans)
def first_3():
    with open('input.txt', 'r') as file:
        for line in file:
            a, b = map(int, line.split())
            with open('output.txt', 'a') as ans:
                ans.write(str(a + b) + '\n')


def first_4():
    with open('input.txt', 'r') as file:
        for line in file:
            a, b = map(int, line.split())
            with open('output.txt', 'a') as ans:
                ans.write(str(a + b * b) + '\n')


def second():
    import sys
    sys.set_int_max_str_digits(0)
    with open('input.txt') as file:
        for line in file:
            n = int(line)
            if n == 0:
                with open('output.txt', 'a') as ans:
                    ans.write('0' + '\n')
            else:
                a = [0, 1]
                for i in range(2, n + 1):
                    x = a[i - 1] + a[i - 2]
                    a.append(x)
                with open('output.txt', 'a') as ans:
                    ans.write(str(a[-1]) + '\n')


def third():

    with open('input.txt') as file:
        for line in file:
            n = int(line)
            if n == 0:
                with open('output.txt', 'a') as ans:
                    ans.write('0' + '\n')
            else:
                a = [0, 1]
                for i in range(2, n + 1):
                    x = a[i - 1] + a[i - 2]
                    if x >= 10:
                        x = x % 10
                    a.append(x)
                with open('output.txt', 'a') as ans:
                    ans.write(str(a[-1]) + '\n')

def time_test():
    import time
    t_start = time.perf_counter()
    print("Время работы %s ", (time.perf_counter() - t_start))
def memory_test(func):
    import sys
    print('Память МБ', sys.getsizeof(func))


second()
time_test()
memory_test(second())