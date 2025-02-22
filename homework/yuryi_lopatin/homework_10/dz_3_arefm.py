first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

def run_calc(func):

    def wrapper(first, second, operation):
        result = func(first, second, operation)
        return result

    return wrapper

@run_calc
def calc(first, second, operation):
    if first == second:
        return first + second
    elif first > second:
        return second - first
    elif second > first:
        return first / second
    elif first < 0 or second < 0:
        return first * second
    else:
        'Введены неверные значения'

print(calc(first, second, '*'))