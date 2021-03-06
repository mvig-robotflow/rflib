import os

jit_option = os.getenv('JIT_OPTION')

def jit(func=None,
            check_input=None,
            full_shape=True,
            derivate=False,
            coderize=False,
            optimize=False):

    def wrapper(func):

        def wrapper_inner(*args, **kargs):
            return func(*args, **kargs)

        return wrapper_inner

    if func is None:
        return wrapper
    else:
        return func


def skip_no_elena(func):

    def wrapper(*args, **kargs):
        return func(*args, **kargs)

    return wrapper
