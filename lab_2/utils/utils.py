import pathlib
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        args += ((int(line),) if len(line.split()) == 1 else ([int(elem) for elem in line.split()],))
    f.close()
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'a')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    f.write(answer)
    f.close()


def work(current_task, func, *dop):
    input_data = f_read(current_task)
    if len(dop) != 0:
        args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(current_task, result)
