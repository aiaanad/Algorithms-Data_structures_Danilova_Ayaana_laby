import pathlib


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

    return string.rstrip()


def convert_list(string):
    list_ = []
    for elem in string.rstrip().split():
        list_.append(convert_one_elem(elem))
    return list_


def is_first_numbers(string):
    if len(string.split()) <= 2:
        l_ = string.split()
        if is_number(l_[0]) and is_number(l_[1]):
            return True
    return False


def convert_first_numbers(string):
    nums = convert_list(string)
    res = ()
    for elem in nums:
        res += (elem,)
    return res


def convert_line(string):
    if len(string.split()) == 1:
        return (convert_one_elem(string),)

    return (convert_list(string),)


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


