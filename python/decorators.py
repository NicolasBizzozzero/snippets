from sys import setrecursionlimit, getrecursionlimit


def timethis(function):
    def wrapper(*arg):
        from time import time
        time_begin = time()
        res = function(*arg)
        time_end = time()
        time_total = time_end - time_begin
        second_or_seconds = "second" if (time_total < 1) else "seconds"
        print("Execution time for \"{}\": {} {}".format(
            function.__name__, time_total, second_or_seconds))
        return res
    return wrapper


def printresult(function):
    def wrapper(*args):
        result = function(*args)
        print("{}{} : {}".format(function.__name__, args, result))
        return result
    return wrapper


def printcallingending(function):
    """ Wrapper used for debugging purposes.
    It print a message before and after calling a function.
    It assure the function has been successfully called.
    """
    def wrapper(*args):
        print("Calling \"{}{}\".".format(function.__name__, args))
        result = function(*args)
        print("Ending  \"{}{}\".".format(function.__name__, args))
        return result
    return wrapper


def memoize(funcion):
    """ Caches a function's return value each
        time it is called. If called later with the same
        arguments, the cached value is returned.
    """
    cache = {}
    miss = object()

    def wrapper(*args):
        # If the result as already be calculated, it's a hit
        result = cache.get(args, miss)
        if result is miss:
            # Else, we call the original function and cache it's result
            result = funcion(*args)
            cache[args] = result
        return result
    return wrapper


@todo_implement
def changestackdepth(function: callable, newsize: int):
    def wrapper(*args):
        oldsize = getrecursionlimit()
        setrecursionlimit(newsize)
        result = function(args[0])
        setrecursionlimit(oldsize)
        return result
    return wrapper


def countinvocations(function):
    """ Wrapper used to count the number of time a function
    has been called. This counter is stored in the attribute
    "invocations" of the wrapped function.
    Example :

        @countinvocations
        def do_something():
            pass

        do_something()
        do_something()
        print(do_something.invocations)     # Print "2"
    """
    def wrapper(*largs, **kargs):
        wrapper.invocations += 1
        function(*largs, **kargs)
    wrapper.invocations = 0
    return wrapper


def get_input_from_file():
    pass


def redirect_output_to_file():
    pass


def force_typing():
    pass


def todo_implement():
    pass


def todo_write_documentation():
    pass


def todo_clean():
    pass


def todo_comment():
    pass


def todo_split_function():
    pass


if __name__ == '__main__':
    @changestackdepth(1000, 1000)
    def fibo(n: int):
        if n == 0 or n == 1:
            return 1
        return fibo(n - 1) + fibo(n - 2)

    print(fibo(10))
