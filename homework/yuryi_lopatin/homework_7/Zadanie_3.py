def process_string(s):
    result = int(s.split()[-1]) + 10
    return result


strings = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9'
]


for s in strings:
    print(process_string(s))
