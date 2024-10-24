def f_read():
    args = ()
    f = open('../txtf/input.txt', 'r')
    for line in f:
        args += ((int(line),) if len(line.split()) == 1 else ([int(elem) for elem in line.split()],))
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
        args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(result)
