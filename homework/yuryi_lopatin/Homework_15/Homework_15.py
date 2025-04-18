import mysql.connector as mysql


db = mysql.connect(
    username='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


def get_student_data(student_id):
    # Запрос оценок
    cursor.execute('SELECT value FROM marks WHERE student_id = %s', (student_id,))
    marks_data = cursor.fetchall()
    print("Оценки:")
    for mark in marks_data:
        print(mark['value'])

    # Запрос книг
    cursor.execute('SELECT title FROM books WHERE taken_by_student_id = %s', (student_id,))
    books_data = cursor.fetchall()
    print("\nКниги:")
    for book in books_data:
        print(book['title'])

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
        LEFT JOIN subjets subj ON l.subject_id = subj.id
        WHERE s.id = %s;""",
        (student_id,)
    )
    data = cursor.fetchall()

    print("\nПолная информация о студенте:")
    for row in data:
        print(f"Id студента: {row['student_id']}")
        print(f"Имя: {row['student_name']}")
        print(f"Фамилия: {row['student_second_name']}")
        print(f"Группа: {row['student_group_id']}")

        print(f"Id группы: {row['group_id']}")
        print(f"Название группы: {row['group_title']}")
        print(f"Начало занятий: {row['group_start_date']}")
        print(f"Окончание занятий: {row['group_end_date']}")

        print(f"Id книги: {row['book_id']}")
        print(f"Название книги: {row['book_title']}")
        print(f"Id студента взявшего книгу: {row['book_taken_by_student_id']}")

        print(f"Id оценки: {row['mark_id']}")
        print(f"Оценка студенту: {row['mark_value']}")
        print(f"Id занятия: {row['mark_lesson_id']}")
        print(f"Id студента: {row['mark_student_id']}")

        print(f"Id занятия: {row['lesson_id']}")
        print(f"Название занятия: {row['lesson_title']}")
        print(f"Id предмета: {row['lesson_subject_id']}")

        print(f"Id предмета: {row['subject_id']}")
        print(f"Название предмета: {row['subject_title']}")
        print("---------------------------------")


student_id = 20198
get_student_data(student_id)

db.close()
