def decorator_example(function: callable) -> callable:
    """ This decorator serve as an example of how you can write decorators. """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
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


@todo_implement
def force_typing(function: callable, *types: type) -> callable:
    """ Throw an exception if the types of the args are differents the types
        in 'types'.
    """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
        return result
    return wrapper


if __name__ == '__main__':
    pass
