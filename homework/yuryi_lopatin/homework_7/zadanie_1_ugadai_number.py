while True:
    user_input = input('Угадайте загаданное число: ')
    number = int(user_input)
    if number == 11:
        break
    else:
        print('попробуйте снова')
print('Поздравляю! Вы угадали!')
