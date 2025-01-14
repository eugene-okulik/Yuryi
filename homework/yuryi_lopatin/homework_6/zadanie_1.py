text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
words = text.split()
for word in words:
    word = word.replace(',', '')
    word = word.replace('.', '')
    print((word) + 'ing')
