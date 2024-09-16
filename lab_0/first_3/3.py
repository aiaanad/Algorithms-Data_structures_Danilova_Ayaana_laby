import sys

with open('input.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        with open('output.txt', 'a') as ans:
            if abs(a) > 10e9 or abs(b) > 10e9:
                ans.write('ncorrect data' + '\n')
            else:
                ans.write(str(a + b) + '\n')
def time_test():
    import time
    t_start = time.perf_counter()
    print("Время работы %s:", (time.perf_counter() - t_start))



time_test()