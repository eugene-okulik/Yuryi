# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

k= 42
l = 57
m = 83
n = 14
#x *2 ** 3 / 2 + y
def calculate (x, y):
    print(x *2 ** 3 / 2 + y)
calculate(k, l)
calculate(l, m)
calculate(m, n)
calculate(n, k)

def calculate_2(x, y):
    result = x * 2 ** 3 / 2 + y
    return result
result_k_l = calculate_2(k, l)
print(result_k_l)
print(calculate_2(k, l))

def work():
    print('i am working')
work()

j = 7
#Если j меньше 5, тогда пишем привет. Иначе j больше, тогде или равно пяти, пишем пока.
#If j < 5 then prin привет. Else j>=5 then print пока
if j < 5:
    print('привет')
else:
    print('пока')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Если j меньше 5, тогда пишем привет, а если (иначе если) от 5 до 10, то печатать Ура Иначе пишем пока.
#If j < 5 then prin привет. Else if j>5 and j<10 then print Ура, Else print пока
if j < 5:
    print('привет')
elif j>5 & j <10:
    print('Ура')
else:
    print('пока')

print('text')
my_text = 'text'

# Напишите функцию, которая распечатает текст "Hello world" если принт петачает пустую строку
# и печатает "Hello Имя", если строка оказалась не пустой
#Если строка пустая, тогда печатать "Hello world", иначе печатать "Hello Yuryi"
#if string  : print ('Hello world'), else: print ('hellow yuryi')
#def printf('yuryi'):
#print(f'Hi, {"Yuryi"}')
#if string '':
#else:
 #   print('Hellow Yuri')


#def print_Hello(name):
        # Use a breakpoint in the code line below to debug your script.
 #       print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # Press the green button in the gutter to run the script.
#    if __name__ == '__main__':
 #       print_hi('PyCharm')
def print_hello(x):
    if x != '':
        print(f"Hello {x}")
    else:
        print("Hello world")


print_hello('')
