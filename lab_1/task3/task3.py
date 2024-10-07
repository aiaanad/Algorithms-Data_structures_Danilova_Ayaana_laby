def insertion_sort():

    n = input().split()

    if len(n) != 1:
        print('---Enter one value---')  #проверка на единственность n
        insertion_sort()  # если данные некорректные функция вызывается повторно
    else:

        if not n[0].isdigit():
            print('---Enter a number---')  # проверка на численное значение n
            insertion_sort()  # если данные некорректные функция вызывается повторно
        else:
            n = int(n[0])
            input_list = [int(elem) for elem in input().split() if elem.isdigit()]  #являются ли значения числовыми

            if not (1 <= n <= 10e3 and len(input_list) == n):
                print('---Incorrect data---')  #проверка на корректность
                insertion_sort()  #если данные некорректные функция вызывается повторно
            else:
                for j in range(1, len(input_list)):
                    key = input_list[j]
                    i = j - 1
                    while i >= 0 and input_list[i] < key:  #направление знака меняется
                        input_list[i + 1], input_list[i] = input_list[i], input_list[i + 1]  #вместо функции swap
                        i = i - 1
                print(' '.join(map(str, input_list)))


insertion_sort()


'''
    Да, алгоритм сортировки вставками можно написать с помощью рекурсии на Python.
    Идея реализации:
        Базовый случай: если размер массива равен 1 или меньше, вернуть значение.
        Рекурсивно отсортировать первые n-1 элементов. 
        Вставить последний элемент на правильную позицию в отсортированном массиве.
'''