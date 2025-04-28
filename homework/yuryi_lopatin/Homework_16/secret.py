import os

import data
from dotenv import load_dotenv
import mysql.connector
import csv

# Загружаем переменные из .env файла
# load_dotenv()
#
# # Получаем переменные окружения
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSW")
# db_host = os.getenv("DB_HOST")
# db_port = os.getenv("DB_PORT")
# db_name = os.getenv("DB_NAME")
#
# # Подключаемся к базе данных
# connection = mysql.connector.connect(
#     host=db_host,
#     user=db_user,
#     password=db_password,
#     database=db_name,
#     port=db_port
# )
#
# # Теперь можно работать с подключением
# cursor = connection.cursor()
# # Ваш код для работы с БД
# # ...
# #cursor = db.cursor(dictionary=True)
#
# query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
# values = ('Yuryl', 'Lo', None)
# cursor.execute(query, values)
# student_id = cursor.lastrowid
# cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
# print(cursor.fetchone())
#
# query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
# values = ('drummers', '1 september', '1_august')
# cursor.execute(query, values)
# group_id = cursor.lastrowid
#
# query = "UPDATE students SET group_id = %s WHERE id = %s"
# cursor.execute(query, (group_id, student_id))
# cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
# print(cursor.fetchone())
#
# # ДОБАВЛЕНИЕ КНИГ - books!!! Вместо пяти отдельных INSERT-запросов
# book_titles = [
#     ('Jim Chapin', student_id),
#     ('Erick Lapton', student_id),
#     ('Shafl', student_id),
#     ('Kononol', student_id),
#     ('Stick control', student_id)
# ]
#
# query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
# cursor.executemany(query, book_titles)
#
# # Если хотим проверить все добавленные книги:
# cursor.execute('SELECT * FROM books WHERE taken_by_student_id = %s', (student_id,))
# print(cursor.fetchall())
#
# # Не забудьте закрыть соединение
# cursor.close()
#connection.close()

# Получаем путь к CSV файлу
it_place = os.path.dirname(__file__)
homew_path = os.path.dirname(os.path.dirname(it_place))
eugene_ok_path = os.path.join(homew_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

#1 распечатает все одной строкой ['name,second_name,group_title,book_title,subject_title,lesson_title,mark_value\n']
with open(eugene_ok_path, 'r', encoding='utf8') as file:
    lines = file.readlines()

print(lines)  # ['name,second_name,group_title,book_title,subject_title,lesson_title,mark_value\n']

#2 <_csv.reader object at 0x00000225ABC9ED40>
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.reader(csv_file)

print(file_data)  # <_csv.reader object at 0x00000225ABC9ED40>

#3 распечатает каждую строку отдельным кортежем ['Petr', 'Ivanov', 'GR_O222', 'Turbo Pascal2', 'SUBD', 'NonSQL DB', '5']
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        print(row) # ['name', 'second_name', 'group_title', 'book_title', 'subject_title', 'lesson_title', 'mark_value']

#4 распечатает все из csv файла отдельной строкой
# name Mark, second_name Pavlov, group_title GR_O111, book_title Python for dumies, subject_title Python
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
        print(f'name {name}, second_name {second_name}, group_title {group_title}, book_title {book_title}, '
              f'subject_title {subject_title}, lesson_title {lesson_title}, mark_value {mark_value}')

#4 фильтрация данных из csv файла по BGPA_107227 распечатает одну строку с такими данными
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        if'BGPA_107227' in row:
            data.append(row)
for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    print(f'name {name}, second_name {second_name}, group_title {group_title}, book_title {book_title}, '
          f'subject_title {subject_title}, lesson_title {lesson_title}, mark_value {mark_value}')

#5 фильтрация данных в виде кортежа - отфильтрует по BGPA_107227
#распечатает ['Ivan', 'Petrov', 'BGPA_107227', 'Turbo Pascal', 'Higher mathematics', 'Math analys', '2']
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        if'BGPA_107227' in row:
            data.append(row)
for row in data:
    print(row)  # ['Ivan', 'Petrov', 'BGPA_107227', 'Turbo Pascal', 'Higher mathematics', 'Math analys', '2']
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    print(f'name {name}, second_name {second_name}, group_title {group_title}, book_title {book_title}, '
          f'subject_title {subject_title}, lesson_title {lesson_title}, mark_value {mark_value}')  # распечатает 1 стр
#name Ivan, second_name Petrov, group_title BGPA_107227, book_title Turbo Pascal, subject_title Higher mathematics

# 6 распечатает все в виде словаря {'name': 'Mark', 'second_name': 'Pavlov'} {'name': 'Ivan', 'second_name': 'Petrov'}
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
for row in data:
    print(row)  # {'name': 'Mark', 'second_name': 'Pavlov'} {'name': 'Ivan', 'second_name': 'Petrov'}

# 7 Фильтр в DictReader работает так же как в reader
# распечатает в виде словаря отфильтрованную строку.
# {'name': 'Ivan', 'second_name': 'Petrov', 'group_title': 'BGPA_107227', 'book_title': 'Turbo Pascal'}
with open(eugene_ok_path, 'r', encoding='utf8', newline= '') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        if row ['group_title'] == 'BGPA_107227':
            data.append(row)
for row in data:
    print(row)  # {'name': 'Ivan', 'second_name': 'Petrov', 'group_title': 'BGPA_107227', 'book_title': 'Turbo Pascal'}