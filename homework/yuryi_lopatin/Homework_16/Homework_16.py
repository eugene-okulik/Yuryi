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
    group_id = row[2]
    book_tittle = row[3]
    subject_title = row[4]
    lesson_title = row[5]
    mark_value = row[6]
    query_group = "SELECT * FROM`groups` g WHERE title = %s"
    values = (row[2],)
    cursor.execute(query_group, values)
    group_result = cursor.fetchall()

    if group_result:
        group_id = group_result[0][0]

        query_student = ("SELECT * FROM students")
    # Запрос всех данных о студенте
        cursor.execute(
            """SELECT
                s.id AS student_id,
                s.name AS student_name,
                s.second_name AS student_second_name,
                s.group_id AS student_group_id,
                g.id AS group_id,
                g.title AS group_title,
                g.start_date AS group_start_date,
                g.end_date AS group_end_date,
                b.id AS book_id,
                b.title AS book_title,
                b.taken_by_student_id AS book_taken_by_student_id,
                m.id AS mark_id,
                m.value AS mark_value,
                m.lesson_id AS mark_lesson_id,
                m.student_id AS mark_student_id,
                l.id AS lesson_id,
                l.title AS lesson_title,
                l.subject_id AS lesson_subject_id,
                subj.id AS subject_id,
                subj.title AS subject_title
            FROM students s
            LEFT JOIN `groups` g ON s.group_id = g.id
            LEFT JOIN books b ON b.taken_by_student_id = s.id
            LEFT JOIN marks m ON m.student_id = s.id
            LEFT JOIN lessons l ON m.lesson_id = l.id
            LEFT JOIN subjets subj ON l.subject_id = subj.id;
            """)
        data = cursor.fetchall()

        print("\nПолная информация о студенте:")
        for row in data:
            print(f"Имя: {row[0]}")
            print(f"Фамилия: {row[1]}")
            print(f"Группа: {row[2]}")

            print(f"Название группы: {row[3]}")

            print(f"Название книги: {row[4]}")
            print(f"Название предмета: {row[5]}")
            print(f"Название занятия: {row[6]}")

            print(f"Оценка студенту: {row[7]}")
            print("---------------------------------")

# print("Проверка данных из CSV файла в базе данных:")
# for row in data:
#     name = row[0]
#     second_name = row[1]
#     group_id = row[2]
#     book_tittle = row[3]
#     subject_title = row[4]
#     lesson_title = row[5]
#     mark_value = row[6]
#     query_group = "SELECT * FROM`groups` g WHERE title = %s"
#     values = (row[2],)
#     cursor.execute(query_group, values)
#     group_result = cursor.fetchall()
#
#     if group_result:
#         group_id = group_result[0][0]
#
#         query_student = ("SELECT * FROM students WHERE group_id = %s")
#         cursor.execute(query_student, (group_id))
#         student_result = cursor.fetchall()
#         if student_result:
#             print(f'Запись найдена: {row[2]}')
#         else:
#             print(f'Запись не найдена:  {row[2]}')
#     else:
#         print(f'Группа не найдена: {row[2]}')
