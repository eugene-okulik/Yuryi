from ctypes import HRESULT

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
a, b, c, d, e = person
print(a, b, c, d, e)


str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

num1 = str1.split(':')[1]
num2 = str2.split(':')[1]
num3 = str3.split(':')[1]

print(int(num1) + 10)
print(int(num2) + 10)
print(int(num3) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
my_text = f'Students {students}, study these subjects: {subjects}'
print(my_text)
