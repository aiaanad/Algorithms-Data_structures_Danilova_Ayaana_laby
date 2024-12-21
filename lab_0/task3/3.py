import time

input_file = 'input.txt'
output_file = 'output.txt'
with open(input_file) as file:
    for line in file:
        n = int(line)
        if not(0 <= n <= 10e7):
            with open(output_file, 'a') as ans:
                ans.write('Incorrect data' + '\n')
        else:
            if n == 0:
                with open(output_file, 'a') as ans:
                    ans.write('0' + '\n')
            else:
                a = [0, 1]
                for i in range(2, n + 1):
                    x = a[i - 1] + a[i - 2]
                    a.append(x % 10)
                with open(output_file, 'a') as ans:
                    ans.write(str(a[-1]) + '\n')

t_start = time.perf_counter()
print("Время работы %s:", (time.perf_counter() - t_start))
