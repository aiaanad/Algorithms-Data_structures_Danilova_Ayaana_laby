def sortland():
    with open('input.txt') as file:
        n = -1
        for line in file:
            if n == -1:
                n = int(line)  # считываем n
                if not (3 <= n <= 9999 and n % 2 != 0):  # случай некорректных данных

                    with open('output.txt', 'w') as ans:
                        ans.write('---Incorrect data---')
                        break
            else:
                data = [float(elem) for elem in line.split() if float(elem) <= 10e6]  # считываем список

                if len(data) != n or len(data) != len(set(data)):  # случай некорректных данных

                    with open('output.txt', 'w') as ans:
                        ans.write('---Incorrect data---')  # случай некорректных данных
                else:
                    id_numbers = [i + 1 for i in range(n)]
                    for i in range(len(data)):  # сортировка пузырьком
                        for j in range(i + 1, len(data)):
                            if data[j] < data[i]:
                                data[i], data[j] = data[j], data[i]
                                id_numbers[i], id_numbers[j] = id_numbers[j], id_numbers[i]

                    with open('output.txt', 'w') as ans:
                        ans.write(str(id_numbers[0]) + ' ' + str(id_numbers[n // 2]) + ' ' + str(id_numbers[n - 1]))


sortland()
