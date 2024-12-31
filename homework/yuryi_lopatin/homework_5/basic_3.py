from ctypes import HRESULT

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
print(type(person))
name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]
print(name, last_name, city, phone, country)

result = [9, 42, 514]
print(result[0] + 10, result[1] + 10, result[2] + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
my_text = f'Students {students}, study these subjects: {subjects}'
print(my_text)
