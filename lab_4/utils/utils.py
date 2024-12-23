import pathlib
from lab_1.utils.utils import base


def work(file, func):
    current_lab = file.parts[-4]
    current_task = file.stem
    read_path = pathlib.Path(__file__).parent.parent.parent.joinpath(current_lab, current_task, 'txtf', 'input.txt')
    write_path = pathlib.Path(__file__).parent.parent.parent.joinpath(current_lab, current_task, 'txtf', 'output.txt')
    base(current_lab, current_task, func, read_path, write_path)



