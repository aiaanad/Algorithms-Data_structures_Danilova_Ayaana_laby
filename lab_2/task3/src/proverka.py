with open('input.txt', 'r') as file:
    n = -1
    for line in file:
        if n == -1:
            if 1 <= int(line) <= 10e3:
                n = int(line)
            else:
                with open('output.txt', 'w') as ans:
                    ans.write('---Incorrect data---')
                    break
        else:
            data = [int(elem) for elem in line.split() if abs(int(elem)) <= 10e9]
            if n != len(data):
                with open('output.txt', 'w') as ans:
                    ans.write('---Incorrect data---')
                    break
            else:
                with open('output.txt', 'a') as ans:
                    s = 0
                    for i in range(n):
                        for j in range(i + 1, n):
                            if data[i] > data[j]:
                                s += 1
                    ans.write(str(s) + '\n')
