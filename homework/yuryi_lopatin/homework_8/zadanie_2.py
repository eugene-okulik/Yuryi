import sys
sys.set_int_max_str_digits(0)

def fibonacci(n):
    fib1, fib2 = 0, 1
    count = 0
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        if count in [5, 200, 1000, 100000]:
            yield fib1

for fib in fibonacci(100001):
    print(fib, end=' ')
print()