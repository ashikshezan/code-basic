from decorators import timer, logger, memoize
from functools import lru_cache

# with recursion (without memoization)


@lru_cache()  # take a parameter "maxsize" and arg should be as a power of 2
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        print(f'Calculating {n}!')
        return fib(n-1) + fib(n-2)


@timer()
def fibonacci_loop(n):
    if n <= 1:
        return 1
    else:
        first = 1
        second = 1
        for index in range(3, n+1):
            first, second = second, first+second

    return second


class Fibonacci:
    '''
    Class implementation of Fibonacci sequence
    '''

    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


def fibonacci_closure():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


s = Fibonacci()
print(s.__hash__())
