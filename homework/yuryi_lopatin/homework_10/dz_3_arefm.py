first = int(input('Enter first number: '))
second = int(input('Enter second number: '))


def run_calc(func):

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        result = func(first, second, operation)

        return result

    return wrapper


@run_calc
def calc(first, second, operation):
    if operation == '*':
        return first * second
    elif operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    else:
        return 'Введены неверные значения'


print(calc(first, second, 'введите число'))