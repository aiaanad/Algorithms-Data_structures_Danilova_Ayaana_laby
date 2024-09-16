with open('input.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        with open('output.txt', 'a') as ans:
            if abs(a) > 10e9 or abs(b) > 10e9:
                ans.write('Incorrect data' + '\n')
            else:
                ans.write(str(a + b ** 2) + '\n')