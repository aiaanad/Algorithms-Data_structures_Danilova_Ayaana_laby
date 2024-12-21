import pathlib
from lab_1.utils.utils import convert_first_numbers, convert_line


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
    if type(answer) is str:
        f.write(answer)
    elif type(answer) is int:
        f.write(str(answer))
    else:
        for elem in answer:
            f.write(f'{elem}\n')
    f.close()


def work(current_task_path, func):
    current_task = current_task_path.stem
    current_lab = current_task_path.parts[-4]

    args = f_read(current_task)
    result = func(*args)
    f_write(current_task, result)

    print(
        f'''LAB NUMBER: {current_lab[4:]}
            TASK NUMBER: {current_task[4:]}
                    INPUT DATA: {args}
                    OUTPUT DATA: {result}

            ''')


