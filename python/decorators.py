def timer(func):
    from time import perf_counter
    from functools import wraps

    @wraps(func)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(i) for i in args]
        kwargs_ = [f'{k} = {v}' for (k, v) in kwargs.items()]
        arg_list = args_ + kwargs_
        args_str = ','.join(arg_list)

        print(f'{func.__name__} ({args_str}) took {elapsed:8f} second(s) to run')
        return result
    return inner


def logger(func):
    from datetime import datetime
    from functools import wraps
    count = 0

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal count
        date = datetime.now()
        result = func(*args, **kwargs)
        count += 1
        print(
            f'Name:{func.__name__} \nLast Call Time:{date}\nNumber of times Declared: {count}')
        return result

    return inner


def memoiz(func):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return inner


if __name__ == "__main__":
    pass
