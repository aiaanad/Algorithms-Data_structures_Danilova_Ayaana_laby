import pathlib
from lab_1.utils.utils import convert_first_numbers, convert_line, f_print


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        if args == () and line[0].isdigit():
            args += convert_first_numbers(line)
        else:
            args += convert_line(line)
    f.close()
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'w')
    if type(answer) is not str:
        if len(answer) > 1:
            answer = ' '.join(map(str, answer)) + '\n'
        else:
            answer = str(answer) + '\n'
    f.write(answer)
    f.close()


def work(current_task_path, func):
    current_task = current_task_path.stem
    current_lab = current_task_path.parts[-4]

    args = f_read(current_task)
    result = func(*args)
    f_write(current_task, result)

    f_print(current_lab, current_task, args, result)



