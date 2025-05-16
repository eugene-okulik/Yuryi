import os
import re


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def find_text_in_files(path, search_text):
    found = False
    for file in get_files(path):
        if os.path.isfile(os.path.join(path, file)):
            try:
                with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_text.upper() in content.upper():  # Поиск без учета регистра для всего содержимого
                        words = re.findall(r'\S+', content)  # Разбиваем текст на слова
                        for i, word in enumerate(words):
                            if search_text.upper() in word.upper():  # Поиск без учета регистра
                                found = True
                                # Определяем границы контекста
                                start = max(0, i - 3)  # 3 слова до
                                end = min(len(words), i + 4)  # 3 слова после + 1

                                # Формируем контекст
                                context = ' '.join(words[start:end])
                                # Выводим результат
                                final_path = os.path.join(path, file)
                                print(f"Найдено '{search_text}' в файле: {final_path}")
                                print(f"Контекст: ...{context}...")
            except UnicodeDecodeError:
                print(f"Не удалось прочитать файл {file} - проблема с кодировкой")

    if not found:
        print(f"Текст '{search_text}' не найден ни в одном файле в директории {path}")


# Запрашиваем у пользователя путь к директории и искомый текст
find_file_path = input("Введите путь к директории для поиска: ")
search_text = input("Введите текст для поиска: ")

# Выполняем поиск
find_text_in_files(find_file_path, search_text)
