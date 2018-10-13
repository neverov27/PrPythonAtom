def cache_decorator(func):
    cache = {}
    
    def f(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return f

@cache_decorator
def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    return fib(n-2)+fib(n-1)
