import time
import tracemalloc


def timeit(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        return result

    return wrapper


def memory(func):
    def wrapper(*args):
        tracemalloc.start()
        result = func(*args)
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()
        return result

    return wrapper


def min_time_memory(func, *args):
    print("Для минимальных значений")
    memory(func)(*args)
    timeit(func)(*args)
    print()


def max_time_memory(func, *args):
    print("Для максимальных значений")
    memory(func)(*args)
    timeit(func)(*args)
    print()
