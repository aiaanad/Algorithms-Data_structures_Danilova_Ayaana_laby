import pathlib


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        line = line.rstrip().split()
        if args == () and line[0].isdigit():
            for elem in line:
                args += (int(elem),)
        else:
            if len(line) == 1 and line[0].isdigit():
                args += (int(line[0]),)
            else:
                args += ([int(elem) if elem.isdigit() else elem for elem in line],)
    f.close()
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'w')
    if type(answer) is str:
        f.write(answer)
    elif type(answer) is int:
        f.write(str(answer))
    else:
        for elem in answer:
            f.write(f'{elem}\n')
    f.close()


def work(current_task_path, func, *dop):
    current_task = current_task_path.stem
    current_lab = current_task_path.parts[-4]
    input_data = f_read(current_task)
    if len(dop) != 0:
        arr = list(input_data) if type(input_data[1]) is not list else input_data[1]
        args = (arr, 0, len(arr) - 1)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(current_task, result)
    print(
        f'''LAB NUMBER: {current_lab[4:]}
            TASK NUMBER: {current_task[4:]}
                    INPUT DATA: {args}
                    OUTPUT DATA: {result}

            ''')


