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
    if len(string.split()) == 2:
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


def f_read(path):
    args = ()
    f = open(path, 'r')
    for line in f:
        if args == () and is_first_numbers(line):
            args += convert_first_numbers(line)
        else:
            args += convert_line(line)
    f.close()
    return args


def f_write(path, answer):
    f = open(path, 'w')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    elif type(answer) is tuple:
        answer = ' '.join(map(str, answer))
    f.write(answer)
    f.close()


def base(current_lab, current_task, func, read_path, write_path, dop=None):
    input_data = f_read(read_path)
    if dop:
        args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
    else:
        args = input_data
    print(
        f'''LAB NUMBER: {current_lab[4:]}
                TASK NUMBER: {current_task[4:]}
                        INPUT DATA: {args}''')

    result = func(*args)
    f_write(write_path, result)
    print(f'''                        OUTPUT DATA: {result}''')


def work(current_lab, current_task, func, dop=None):
    read_path = pathlib.Path(__file__).parent.parent.parent.joinpath(current_lab, current_task, 'txtf', 'input.txt')
    write_path = pathlib.Path(__file__).parent.parent.parent.joinpath(current_lab, current_task, 'txtf', 'output.txt')
    base(current_lab, current_task, func, read_path, write_path, dop)
