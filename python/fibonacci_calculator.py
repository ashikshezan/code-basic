from decorators import timer, logger, memoiz

# with recursion (without memoization)


def fib(n):
    if n <= 2:
        return 1
    else:
        print(f'Calculating {n}!')
        return fib(n-1) + fib(n-2)


@memoiz
def fibonacci_recursive(n):
    return fib(n)


@logger
@timer
def fibonacci_loop(n):
    if n <= 1:
        return 1
    else:
        first = 1
        second = 1
        for index in range(3, n+1):
            first, second = second, first+second

    return second


# class Fibonacci:
#     def __init__(self):
#         self.cache = {1: 1, 2: 1}

#     def fib(self, n):
#         if n not in self.cache:
#             self.cache[n] = self.fib(n-1) + self.fib(n-2)
#         return self.cache[n]


# def fib():
#     cache = {1: 1, 2: 1}

#     def calc_fib(n):
#         if n not in cache:
#             cache[n] = calc_fib(n-1) + calc_fib(n-2)
#         return cache[n]
#     return calc_fib


print(fibonacci_recursive(11))
print('asd')
print(fibonacci_recursive(14))
