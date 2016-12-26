def decorator_example(function: callable) -> callable:
    """ This decorator serve as an example of how you can write decorators. """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
        return result
    return wrapper


def quiet(function: callable) -> callable:
    """ Redirect stdout to nothing. """
    def wrapper(*args, **kwargs):
        from os import devnull
        import sys

        previous_stdout = sys.stdout
        sys.stdout = open(devnull, 'w')
        result = function(*args, **kwargs)
        sys.stdout = previous_stdout
        return result
    return wrapper


def todo_implement(function: callable) -> callable:
    """ Print an explicative message about the fact that this function is not
        implemented, then stop the function from being called.
    """
    def wrapper(*args, **kwargs):
        print(("\"{}\" is currently not implemented correctly and therefore "
               "will not be called.").format(function.__name__))
    return wrapper


def todo_improve(function: callable) -> callable:
    """ Print an explicative message about the fact that this function needs to
        be improved.
    """
    def wrapper(*args, **kwargs):
        print("\"{}\" needs to be improved.".format(
            function.__name__))
        return function(*args, **kwargs)
    return wrapper


def todo_refactor(function: callable) -> callable:
    """ Print an explicative message about the fact that this function needs to
        be refactored.
    """
    def wrapper(*args, **kwargs):
        print("\"{}\" needs to be refactored.".format(function.__name__))
        return function(*args, **kwargs)
    return wrapper


@todo_implement
def todo_clean():
    pass


@todo_implement
def todo_comment():
    pass


@todo_implement
def todo_split_function():
    pass


@todo_implement
def todo_write_documentation():
    pass


def print_warning(*reasons: str) -> callable:
    """ Print a list of reasons as why executing this function is unsafe.
        This act as a warning for dangerous functions or not correctly
        implemented functions.
    """
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("/!\\ WARNING /!\\")
            print("Using \"{}\" is unsafe for the following reason{} :".format(
                function.__name__, "s" if len(reasons) > 1 else ""))
            for reason in reasons:
                print("- {}".format(reason))
            input(("If you still want to execute this function, press enter to"
                   " continue."))
            return function(*args)
        return wrapper
    return real_decorator


def time_this(function: callable) -> callable:
    """ Print the execution time of the wrapped function. """
    def wrapper(*args):
        from time import time
        time_begin = time()
        result = function(*args)
        time_end = time()
        time_total = time_end - time_begin
        second_or_seconds = "second" if (time_total < 1) else "seconds"
        print("Execution time for \"{}\": {} {}".format(
            function.__name__, time_total, second_or_seconds))
        return result
    return wrapper


def count_invocations(function: callable) -> callable:
    """ Add the "invocations" attribute to the wrapped function which will be
        incremented each time the function is called.
        Example :
        >>> print(f.invocations)
        0
        >>> f(4)
        >>> print(f.invocations)
        1
        >>> f(4)
        >>> print(f.invocations)
        2
    """
    def wrapper(*args, **kargs):
        wrapper.invocations += 1
        function(*args, **kargs)
    wrapper.invocations = 0
    return wrapper


def print_result(function: callable) -> callable:
    """ Print the call of the wrapped function followed by its result.
        Example :
        >>> fibo(6)
        fibo(6) : 8
        >>> add(4, 18)
        add(4, 18) : 22

    """
    def wrapper(*args):
        from nbu_string import concatenation
        result = function(*args)
        # Remove the useless coma if there is just one argument
        arg_or_args = None
        if len(args) == 1:
            arg_or_args = concatenation(str(args)[:-2], ')')
        else:
            arg_or_args = args
        print("{}{} : {}".format(function.__name__, arg_or_args, result))
        return result
    return wrapper


def print_calling_ending(function: callable) -> callable:
    """ Print a message before and after calling a function.
        It assures the function has been successfully called.
        Example :
        >>> @print_calling_ending
        >>> def add(a, b) -> int:
        >>>     print("I'm in the function !")
        >>>     return a + b
        >>> add(4, 18)
        Calling "add(4, 18)"
        I'm in the function !
        Ending  "add(4, 18)"

    """
    def wrapper(*args):
        print("Calling \"{}{}\"".format(function.__name__, args))
        result = function(*args)
        print("Ending  \"{}{}\"".format(function.__name__, args))
        return result
    return wrapper


def memoize(function: callable) -> callable:
    """ Caches a function's return value each time it is called.
        If called later with the same  arguments, the cached value is returned.
    """
    cache = {}
    miss = object()

    def wrapper(*args):
        # If the result as already be calculated, it's a hit
        result = cache.get(args, miss)
        if result is miss:
            # Else, we call the original function and cache it's result
            result = function(*args)
            cache[args] = result
        return result
    return wrapper


def change_stack_depth(new_size: int) -> callable:
    """ Change the recursion limit to new_size before calling the function,
        then reset its original value after calling the function.
    """
    def real_decorator(function: callable) -> callable:
        def wrapper(*args):
            from sys import setrecursionlimit, getrecursionlimit
            old_size = getrecursionlimit()
            setrecursionlimit(new_size)
            result = function(*args)
            setrecursionlimit(old_size)
            return result
        return wrapper
    return real_decorator


def set_stdout_to_file(new_stdout: str, mode: str = 'w') -> callable:
    """ Temporary change stdout to the file value passed as argument. """
    def real_decorator(function: callable) -> callable:
        def wrapper(*args):
            import sys

            previous_stdout = sys.stdout
            sys.stdout = open(new_stdout, mode)
            result = function(*args)
            sys.stdout = previous_stdout
            return result
        return wrapper
    return real_decorator


def set_stdin_from_str(new_stdin: str) -> callable:
    """ Temporary change stdin to the string value passed as argument. """
    def real_decorator(function: callable) -> callable:
        def wrapper(*args):
            import sys
            from io import StringIO

            previous_stdin = sys.stdin
            sys.stdin = StringIO(new_stdin)
            result = function(*args)
            sys.stdin = previous_stdin
            return result
        return wrapper
    return real_decorator


def set_stdin_from_file(new_stdin: str, mode: str = 'r') -> callable:
    """ Temporary change stdin to the file value passed as argument. """
    def real_decorator(function: callable) -> callable:
        def wrapper(*args):
            import sys

            previous_stdin = sys.stdin
            sys.stdin = open(new_stdin, mode)
            result = function(*args)
            sys.stdin = previous_stdin
            return result
        return wrapper
    return real_decorator


@todo_implement
def force_typing(function: callable, *types: type) -> callable:
    """ Throw an exception if the types of the args are differents than the
        types in 'types'.
    """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
        return result
    return wrapper


if __name__ == '__main__':
    pass
