import sys
sys.set_int_max_str_digits(0)

rng = [5, 200, 1000, 100000]
#Этот генератор должен только выдавать последовательность чисел фибоначчи
def fibonacci(n, rng):
    fib1, fib2 = 0, 1
    count = 0
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        if count in rng:
            yield fib1

#А здесь, пользуясь генератором нужно получать числа и распечатывать только те, которые нужны.
for fib in fibonacci(100001, rng):
    print(fib, end=' ')
print()

