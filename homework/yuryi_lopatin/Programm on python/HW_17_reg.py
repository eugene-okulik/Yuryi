#!/usr/bin/env python3
'''
Скрипт для поиска текста в файлах
'''
# ИМПОРТЫ:
# Основные библиотеки для работы с файловой системой и регулярными выражениями
import os       # для работы с путями и файловой системой
import re       # для регулярных выражений (пока не используется)
import sys      # для доступа к аргументам командной строки
import argparse # для удобного разбора аргументов командной строки (пока не используется)
from calendar import error

base_path = os.path.dirname(__file__)   # запишет текущий рабочий каталога в переменную base_path
homew_path = os.path.dirname(os.path.dirname(base_path)) # Переход на папку выше
file_path = os.path.join(homew_path, 'eugene_okulik', 'data', 'logs') # Формирование пути к каталогу с логами

# ПОИСК ФАЙЛОВ:
result = []  # Создаем пустой список, который будет хранить результаты поиска. В список будут добавляться индексы

def get_files(path, search_text=None):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
for file in get_files(file_path, 'error'):
    search_text = "ERROR"
    with open(os.path.join(file_path, file), 'r', encoding='utf-8') as f:
        content = f.read()
        if search_text in content:
            words = re.findall(r'\S+', content)  # Разбиваем текст на слова
            for i, word in enumerate(words):
                if search_text in word.upper():  # Поиск без учета регистра
                    start = max(0, i - 3)  # Определяем границы контекста 3 слова до
                    end = min(len(words), i + 4)  # Определяем границы контекста 3 слова после + 1
                    context = ' '.join(words[start:end])  # Формируем контекст
                    final_path = os.path.join(file_path, file)  # Выводим результат
                    print(f"Найдено 'ERROR' в файле: {final_path}")
                    print(f"Контекст: ...{context}...")
