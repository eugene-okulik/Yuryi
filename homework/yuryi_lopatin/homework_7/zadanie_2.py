words = {'I': 3, 'love': 5, 'Python': 1, '!': 50} # Словарь с парами слово: количество

def words_number(dictionary):
    for word, num in dictionary.items():
        print(f'{word * num}')

words_number(words)
