def add_text_after_run(func):

    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result

    return wrapper


@add_text_after_run
def simple1():
    print('simple1')


@add_text_after_run
def simple2():
    print('simple2')


@add_text_after_run
def print_nothong():
    return 'hello'


@add_text_after_run
def calc(x):
    print(x * 2)


@add_text_after_run
def calc2(x, y):
    print(x * y)


@add_text_after_run
def one_more_func(*args):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9)


@add_text_after_run
def example(text):
    print(text)


simple1()
simple2()
print(print_nothong())
calc(3)
calc2(3, 5)
one_more_func()
example('print me')
