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

        query_student = "SELECT * FROM students WHERE name = %s AND second_name = %s AND group_id = %s"
        cursor.execute(query_student, (row[0], row[1], group_id))
        student_result = cursor.fetchall()
        if student_result:
            print(f'Запись найдена: {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')
        else:
            print(f'Запись не найдена: {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')
    else:
        print(f'Группа не найдена: {row[2]}')
