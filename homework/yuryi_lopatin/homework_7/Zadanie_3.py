str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

list_from_str1 = str1.split(' ')
list_from_str2 = str2.split(' ')
list_from_str3 = str3.split(' ')

numbers1 = list_from_str1[-1] # <class 'str'> 42
numbers2 = list_from_str2[-1] # <class 'str'> 514
numbers3 = list_from_str3[-1] # <class 'str'> 9

print(int(numbers1) + 10)
print(int(numbers2) + 10)
print(int(numbers3) + 10)