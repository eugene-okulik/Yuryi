words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def words_number(dictionary):  # в скобках аргументы, называй как угодно, но потом соблюдай порядок
    for word, num in dictionary.items():
        result = ''
        i = 0
        while i < num:
            result += word + ' '
            i += 1
        print(result)


words_number(words)
