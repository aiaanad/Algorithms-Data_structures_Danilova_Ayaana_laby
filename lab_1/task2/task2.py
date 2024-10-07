def insertion_sort():
    n = input().split()

    if len(n) != 1:
        print('---Enter one value---')  # проверка на единственность n
        insertion_sort()  # если данные некорректные функция вызывается повторно
    else:

        if not n[0].isdigit():
            print('---Enter a number---')  # проверка на численное значение n
            insertion_sort()  # если данные некорректные функция вызывается повторно
        else:
            n = int(n[0])
            input_list = [int(elem) for elem in input().split() if elem.isdigit()]  # являются ли значения числовыми

            if not (1 <= n <= 10e3 and len(input_list) == n):
                print('---Incorrect data---')  # проверка на корректность
                insertion_sort()  # если данные некорректные функция вызывается повторно
            else:
                new_index = [1]  # создаем список новых индексов
                for j in range(1, len(input_list)):
                    key = input_list[j]
                    i = j - 1
                    while i >= 0 and input_list[i] > key:
                        input_list[i + 1] = input_list[i]
                        i = i - 1
                    input_list[i + 1] = key
                    new_index.append(i + 2)  # прибавляется 1, т.к. в питоне нумерация начинаеся с 0, а необходимо с 1
                print(' '.join(map(str, new_index)), '\n', ' '.join(map(str, input_list)), sep='')


insertion_sort()
