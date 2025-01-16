text: str = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
    'dignissim vitae libero.')
words = text.split()
final_text = []

for word in words:
    if word[-1] in ',.':
        punctution = word[-1]
        main_word = word[:-1] + 'ing' + punctution
    else:
        main_word = word + 'ing'
    final_text.append(main_word)
print(' '.join(final_text))
