from functools import wraps


def buffer(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*arg):
        result = cache.get(arg)
        if result is None:
            cache[arg] = result = fn(*arg)
        return result

    return wrapper


@buffer
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(count):
    n, a, b = 0, 0, 1
    while n < count:
        yield b
        a, b = b, a + b
        n += 1
