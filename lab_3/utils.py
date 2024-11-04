def f_read():
    args = ()
    f = open('../txtf/input.txt', 'r')
    arr = []
    for line in f:
        line = line.rstrip()
        if args == ():
            args += (int(line),) if len(line.split()) == 1 else tuple([int(elem) for elem in line.split()])
        else:
            if line.split()[0][1:].isdigit() or line.split()[0].isdigit():
                arr.append((int(line) if len(line.split()) == 1 else [int(elem) for elem in line.split()]))
            else:
                arr.append([elem for elem in line])
    args += tuple(arr) if len(arr) <= 1 else (arr,)
    f.close()
    return args


def f_write(answer):
    f = open('../txtf/output.txt', 'a')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    f.write(answer)
    f.close()


def work(func, *dop):
    input_data = f_read()
    if len(dop) != 0:
        arr = list(input_data) if type(input_data[1]) is not list else input_data[1]
        args = (arr, 0, len(arr) - 1)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(result)
