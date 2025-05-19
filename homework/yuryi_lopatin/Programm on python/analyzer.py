import os
import re
import argparse


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
                    lines = f.readlines()
                    for line_num, line in enumerate(lines, 1):  # Нумерация строк с 1
                        if search_text.upper() in line.upper():  # Поиск без учета регистра для всего содержимого
                            found = True
                            final_path = os.path.join(path, file)
                            words = re.findall(r'\S+', line)  # Разбиваем текст на слова
                            for i, word in enumerate(words):  # Ищем слово, содержащее искомый текст
                                if search_text.upper() in word.upper():  # Поиск без учета регистра
                                    # Определяем границы контекста
                                    start = max(0, i - 3)  # 3 слова до
                                    end = min(len(words), i + 4)  # 3 слова после +
                                    # Формируем контекст
                                    context = ' '.join(words[start:end])
                                    # Выводим результат
                                    final_path = os.path.join(path, file)
                                    print(f"Найдено '{search_text}' в файле: {final_path}")
                                    print(f"Строка №{line_num}: Контекст: ...{context}...")
                                    print("-" * 50)
                                    break  # Переходим к следующей строке после нахождения первого контекста
            except UnicodeDecodeError:
                print(f"Не удалось прочитать файл {file} - проблема с кодировкой")

    if not found:
        print(f"Текст '{search_text}' не найден ни в одном файле в директории {path}")

# Создаем парсер аргументов командной строки
def main():
    parser = argparse.ArgumentParser(description='Поиск текста в файлах указанной директории')
    parser.add_argument('path', type=str, help='Путь к директории для поиска')  # позиционный арг
    parser.add_argument('--text', type=str, required=True, help='Текст для поиска')  # именованный арг
    args = parser.parse_args()
    find_text_in_files(args.path, args.text)

if __name__=="__main__":
    main()

# # Запрашиваем у пользователя путь к директории и искомый текст
# eugene_okulik_path = input("Введите путь к директории для поиска: ")
# search_text = input("Введите текст для поиска: ")
#
# # Выполняем поиск
# find_text_in_files(eugene_okulik_path, search_text)
