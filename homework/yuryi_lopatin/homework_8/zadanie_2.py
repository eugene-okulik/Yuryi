import sys
sys.set_int_max_str_digits(0)


rng = [5, 200, 1000, 100000]


def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


count = 0
found_numbers = 0
for fib in fibonacci():
    count += 1
    if count in rng:
        print(fib)
        found_numbers += 1
        if found_numbers==len(rng):
            break
