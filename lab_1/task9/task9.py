def binary_addition():
    with open('input.txt', 'r') as file:
        for line in file:
            input_data = [elem for elem in line.split()]

    a = [int(elem) for elem in input_data[0]]  # первое число, каждая цифра которого явл элементом списка а
    b = [int(elem) for elem in input_data[1]]  # второе число, каждая цифра которого явл элементом списка b
    if not (len(a) == len(b) and 0 <= len(a) <= 10e3):  # проверка на корректность
        with open('output.txt', 'w') as ans:
            ans.write('---Incorrect data---')
    else:
        n = len(a)
        c = [0 for i in range(n + 1)]  # заполним список с нулями
        for i in range(n, 0, -1):  # начнем заполнять с конца
            c[i] = (c[i] + a[i - 1] + b[i - 1]) % 2
            c[i - 1] += (a[i - 1] + b[i - 1]) // 2
        with open('output.txt', 'w') as ans:
            ans.write(''.join(map(str, c)))


binary_addition()
