from decorator_timer import timer

# with recursion (without memoization)
@timer
def fib(n):
    if n <= 1:
        return 1

    else:
        return fib(n-1) + fib(n-2)
