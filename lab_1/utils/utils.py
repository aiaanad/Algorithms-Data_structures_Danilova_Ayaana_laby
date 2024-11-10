import pathlib
import os
import sys
from difflib import SequenceMatcher
sys.path.append(os.path.join(os.getcwd(), '..'))


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        if SequenceMatcher(None, line, '0123456789').ratio() != 0:
            args += (((int(line) if '.' not in line else float(line)),) if len(line.split()) == 1 else
                    ([(int(elem) if '.' not in line else float(elem)) for elem in line.split()],))
        else:
            args += ([elem for elem in line],)
    f.close()
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'a')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    elif type(answer) is tuple:
        answer = ' '.join(map(str, answer))
    f.write(answer)
    f.close()


def work(current_task, func, dop=None):
    input_data = f_read(current_task)
    args = None
    if dop is not None:
        if dop == 0:
            args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
        if dop == 1:
            input_data[0][0] = [input_data[0][0] // 10 ** i % 10 for i in range(len(str(input_data[0][0])) - 1, -1, -1)]
            input_data[0][1] = [input_data[0][1] // 10 ** i % 10 for i in range(len(str(input_data[0][1])) - 1, -1, -1)]
            args = input_data[0][0], input_data[0][1]
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(current_task, result)





