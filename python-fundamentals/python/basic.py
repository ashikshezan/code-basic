from functools import wraps


def counter(func):
    count = 0
    @wraps(func)  # by this the instrospection info of inner is overriden by mult()
    def innerFunc(*args,  **kwargs):
        nonlocal count
        count += 1
        print(f'{func.__name__} is called {count} time(s)')
        return func(*args,  **kwargs)

    return innerFunc


@counter
def mult(a, b, c=1):
    """
    return the product
    """
    return a*b*c
