import pathlib
import os
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def convert_one_elem(string):
    if is_number(string):
        if '.' in string:
            return float(string)
        return int(string)

    return string


def convert_list(string):
    list_ = []
    for elem in string.rstrip().split():
        list_.append(convert_one_elem(elem))
    return list_


def convert_line(string):
    if len(string.split()) == 1:
        return (convert_one_elem(string),)
    return (convert_list(string), )


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        args += convert_line(line)
    f.close()
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
    input_data = f_read(current_task)
    if len(dop) != 0:
        args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(current_task, result)
    print(
        f'''LABA_NUMBER: {current_lab[4:]}
        TASK NUMBER: {current_task[4:]}
                INPUT DATA: {args}
                OUTPUT DATA: {result}

        ''')
