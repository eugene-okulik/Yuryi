person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone_number, state = person
print(name, last_name, city, phone_number, state)


str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

num1 = (str1.index('42'))
num2 = (str2.index('514'))
num3 = (str3.index('9'))

print(int(num1) + 10)
print(int(num2) + 10)
print(int(num3) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
my_text = f'Students {students}, study these subjects: {subjects}'
print(my_text)
