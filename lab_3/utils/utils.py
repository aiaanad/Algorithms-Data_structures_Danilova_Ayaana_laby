import pathlib
from lab_1.utils.utils import convert_line


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        args += convert_line(line)
    f.close()
    print(args)
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'w')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    f.write(answer)
    f.close()


def work(current_lab, current_task, func, *dop):
    args = f_read(current_task)
    if len(dop) != 0:
        args = args[-1], 0, len(args[-1]) - 1

    result = func(*args)
    f_write(current_task, result)
    print(
        f'''LABA_NUMBER: {current_lab[4:]}
            TASK NUMBER: {current_task[4:]}
                    INPUT DATA: {args}
                    OUTPUT DATA: {result}

            ''')
