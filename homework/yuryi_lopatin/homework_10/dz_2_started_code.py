def repeat_run(func):

    def wrapper(*args, count=1):
        for i in range(count):
            result = func(*args)
        return result

    return wrapper


@repeat_run
def simple1():
    print('simple1')


@repeat_run
def simple2():
    print('simple2')


@repeat_run
def calc(x):
    print(x * 2)


@repeat_run
def calc2(x, y):
    print(x * y)


@repeat_run
def one_more_func(*args):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9)


@repeat_run
def example(text):
    print(text)

simple1(count=2)
simple2(count=2)
calc(3, count=2)
calc2(3, 5, count=2)
one_more_func(count=2)
example('print me', count=2)
