import os
import csv
from dotenv import load_dotenv
import mysql.connector


# Получаем путь к CSV файлу
it_place = os.path.dirname(__file__)
homew_path = os.path.dirname(os.path.dirname(it_place))
eugene_ok_path = os.path.join(homew_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Загружаем переменные из .env файла
load_dotenv()

# Получаем переменные окружения
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSW")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# читаем данные из csv файла
with open(eugene_ok_path, 'r', encoding='utf8', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    headers = next(file_data)  # Если закоментить, выдаст заголовки (имя, фамилия, груп ид и т.)
    data = []
    for row in file_data:
        data.append(row)

# Подключаемся к базе данных
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=db_port
)

cursor = connection.cursor()

print("Проверка данных из CSV файла в базе данных:")
for row in data:
    name = row[0]
    second_name = row[1]
    group_title = row[2]
    book_tittle = row[3]
    subject_title = row[4]
    lesson_title = row[5]
    mark_value = row[6]

    query_group = "SELECT * FROM`groups` g WHERE title = %s"
    values = (row[2],)
    cursor.execute(query_group, (group_title,))
    group_result = cursor.fetchall()

    if group_result:
        group_id = group_result[0][0]

        query_student = "SELECT * FROM students WHERE name = %s AND second_name = %s AND group_id = %s"
        cursor.execute(query_student, (name, second_name, group_id))
        student_result = cursor.fetchall()
        if student_result:
            print(f'Запись найдена: {row[2]}')
            student_id = student_result[0][0]
        else:
            print(f'Запись не найдена:  {row[2]}')
            continue

        query_book = "SELECT * FROM books WHERE title = %s AND taken_by_student_id = %s"
        cursor.execute(query_book, (book_tittle, student_id))
        book_result = cursor.fetchall()
        if book_result:
            print(f'Запись найдена: {row[3]}')
            book_id = book_result[0][0]
        else:
            print(f'Запись не найдена:  {row[3]}')
            continue

        query_subjet = "SELECT * FROM subjets WHERE title = %s"
        cursor.execute(query_subjet, (subject_title,))
        subjet_result = cursor.fetchall()
        if subjet_result:
            print(f'Запись найдена: {row[4]}')
            subject_id = subjet_result[0][0]
        else:
            print(f'Запись не найдена:  {row[4]}')
            continue

        query_lesson = "SELECT * FROM lessons WHERE title = %s AND subject_id = %s"
        cursor.execute(query_lesson, (lesson_title, subject_id))
        lesson_result = cursor.fetchall()
        if lesson_result:
            print(f'Запись найдена: {row[5]}')
            lesson_id = lesson_result[0][0]
        else:
            print(f'Запись не найдена:  {row[5]}')
            continue

        query_mark = "SELECT * FROM marks WHERE student_id = %s AND lesson_id = %s AND value = %s"
        cursor.execute(query_mark, (student_id, lesson_id, mark_value))
        mark_result = cursor.fetchall()
        if mark_result:
            print(f'Запись найдена: {row[6]}')
            mark_id = mark_result[0][0]
        else:
            print(f'Запись не найдена:  {row[6]}')
            continue

    else:
        print(f'Группа не найдена: {row[2]}')
