first = int(input('Enter first number: '))
second = int(input('Enter second number: '))


def run_calc(func):

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            result = first * second
        elif first == second:
            result = first + second
        elif first > second:
            result = second - first
        elif second > first:
            result = first / second

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


print(calc(first, second, 'operation'))
