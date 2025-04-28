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
    query_group = "SELECT * FROM`groups` g WHERE title = %s"
    values = (row[2],)
    cursor.execute(query_group, values)
    group_result = cursor.fetchall()

    if group_result:
        print(f'Группа найдена: {row[2]}')
    else:
        print(f'Группа не найдена: {row[2]}')
