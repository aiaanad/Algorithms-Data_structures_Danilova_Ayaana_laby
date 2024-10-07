with open('input.txt') as file:
    n = -1
    for line in file:
        if n == -1:
            n = int(line)  # считываем n
            if not 1 <= n <= 10e5:  # случай некорректных данных

                with open('output.txt', 'w') as ans:
                    ans.write('---Incorrect data---')
        else:
            data = [elem for elem in line]  # считываем список

            if len(data) != n:

                with open('output.txt', 'w') as ans:
                    ans.write('---Incorrect data---')  # случай некорректных данных
            else:
                for i in range(n):  # сортировка пузырьком
                    for j in range(i + 1, len(data)):
                        if data[j] < data[i]:
                            data[i], data[j] = data[j], data[i]

                mid = 'a'
                for i in range(n):
                    if data.count(data[i]) % 2 != 0 and data[i] < mid:
                        mid = data[i]
                        break
                    mid = ''  # средний элемент

                right = []  # правая часть ответа
                left = []  # левая
                for elem in data:
                    kolvo = left.count(elem) + right.count(elem)  # количество в правой и левой части
                    if kolvo % 2 == 0:
                        if data.count(elem) - kolvo > 1:
                            left.append(elem)
                    else:
                        right.append(elem)
                with open('output.txt', 'w') as ans:
                    ans.write(''.join(left) + mid + ''.join(right[::-1]))
