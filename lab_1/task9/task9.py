def binary_addition():

    input_data = input().split()

    if len(input_data) != 2:  #проверка на то, что введены ровно два числа
        print('---Incorrect data---')
        binary_addition()  #если данные некорректные функция вызывается повторно
    else:
        a = [int(elem) for elem in input_data[0]]  #первое число, каждая цифра которого явл элементом списка а
        b = [int(elem) for elem in input_data[1]]  #второе число, каждая цифра которого явл элементом списка b

        digits_number = (a + b).count(1) + (a + b).count(0)  #проверка на бинарность чисел

        if not (len(a) == len(b) and 0 <= len(a) <= 10e3 and digits_number == 2 * len(a)):  #проверка на корректность
            print('---Incorrect data---')
            binary_addition()  #если данные некорректные функция вызывается повторно
        else:
            n = len(a)
            c = [0 for i in range(n + 1)]  #заполним список с нулями
            for i in range(n, 0, -1):  #начнем заполнять с конца
                c[i] = (c[i] + a[i - 1] + b[i - 1]) % 2
                c[i - 1] += (a[i - 1] + b[i - 1]) // 2
            print(''.join(map(str, c)))


binary_addition()
