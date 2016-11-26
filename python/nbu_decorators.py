def decorator_example(function: callable) -> callable:
    """ This decorator serve as an example of how you can
        write decorators.
    """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
        return result
    return wrapper


def todo_implement(function: callable) -> callable:
    """ Print an explicative message about the fact that
        this function is not implemented, then stop the
        function to be called.
    """
    def wrapper(*args, **kwargs):
        print("\"{}\" is currently not implemented correctly and therefore will not be called.".format(function.__name__))
    return wrapper


def todo_improve(function: callable) -> callable:
    """ Print an explicative message about the fact that
        this function needs to be improved.
    """
    def wrapper(*args, **kwargs):
        print("\"{}\" is too sloww, it needs to be improved.".format(function.__name__))
        return function(*args, **kwargs)
    return wrapper


def todo_refactor(function: callable) -> callable:
    """ Print an explicative message about the fact that
        this function needs to be refactored.
    """
    def wrapper(*args, **kwargs):
        print("\"{}\" needs to be refactored.".format(function.__name__))
        return function(*args, **kwargs)
    return wrapper


def print_warning(*reasons):
    """ Print a list of reasons as why executing this function is unsafe.
        This act as a warning for dangerous functions or not correctly
        implemented functions.
    """
    def real_decorator(function):    
        def wrapper(*args, **kwargs):
            print("/!\\ WARNING /!\\")
            print("Using \"{}\" is unsafe for the following reason{} :".format(function.__name__, "s" if len(reasons) > 1 else ""))
            for reason in reasons:
                print("- {}".format(reason))
            input("If you still want to execute this function, press enter to continue.")
            return function(*args)
        return wrapper
    return real_decorator


@todo_implement
def force_typing(function, *types):
    """ Throw an exception if the types
        of the args are differents the types in 'types'.
    """
    def wrapper(*args, **kwargs):
        # Instructions here will be executed before calling the function
        result = function(*args, **kwargs)
        # Instructions here will be executed after calling the function
        return result
    return wrapper


if __name__ == '__main__':
    pass
