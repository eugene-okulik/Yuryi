class Book():
    have_text = True

<<<<<<< HEAD
    def __init__(self, title, author, pages, material, reserve):
=======
    def __init__(self, title, author, pages, material, isbn, reserve):
>>>>>>> 6a9ebe5236ef470b04e4ceb6ebf59917d01dc7af
        self.title = title
        self.author = author
        self.pages = pages
        self.material = material
<<<<<<< HEAD
=======
        self.isbn = isbn
>>>>>>> 6a9ebe5236ef470b04e4ceb6ebf59917d01dc7af
        self.reserve = reserve

    def print(self):
        if self.reserve:
<<<<<<< HEAD
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}:, материал: {self.material} зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}')

class SchoolBook(Book):
    def __init__(self, title, author, pages, book_type, reserve, subject, school_class, homework):
        super().__init__(title, author, pages, book_type, reserve)
=======
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}:, материал: {self.material}, '
                    f'isbn: {self.isbn}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}, '
                    f'isbn: {self.isbn}')


class SchoolBook(Book):
    def __init__(self, title, author, pages, book_type, isbn, reserve, subject, school_class, homework):
        super().__init__(title, author, pages, book_type, isbn, reserve)
>>>>>>> 6a9ebe5236ef470b04e4ceb6ebf59917d01dc7af
        self.subject = subject
        self.school_class = school_class
        self.homework = homework

    def print(self):
        if self.homework:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                    f'класс: {self.school_class}, зарезервирована')
        else:
<<<<<<< HEAD
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, класс: {self.school_class}')

matematika_5_class = SchoolBook('Математика', 'Евклид', 211, 'school book', True, 'математика', 5, True)
geography = SchoolBook('География', 'Колумб', 240, 'school book', False, 'география', 7, False)
history = SchoolBook('История', 'Герадот', 210, 'school book',False, 'история', 9, False)

club_5_am = Book('Клуб 5 утра', 'Шарма', 511, 'бумага', True)
idiot = Book('Идиот', 'Достоевский', 640, 'бумага', False)
ispoved_huligana = Book('Исповедь хулигана', 'Есенин', 320, 'бумага',
                       False)
steve_jobs = Book('Стив Джобс', 'Исаксон', 610, 'бумага',
                  False)
cats_hause = Book('Кошкин дом', 'Маршак', 42, 'бумага', False)

=======
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                    f'класс: {self.school_class}')


matematika_5_class = SchoolBook('Математика', 'Евклид', 211, 'school book', 2128511,
                                True, 'математика', 5, True)
geography = SchoolBook('География', 'Колумб', 240, 'school book', 2128512,
                       False, 'география', 7, False)
history = SchoolBook('История', 'Герадот', 210, 'school book', 2128513, False,
                     'история', 9, False)

club_5_am = Book('Клуб 5 утра', 'Шарма', 511, 'бумага', 2128506, True)
idiot = Book('Идиот', 'Достоевский', 640, 'бумага', 2128507, False)
ispoved_huligana = Book('Исповедь хулигана', 'Есенин', 320, 'бумага', 2128508, False)
steve_jobs = Book('Стив Джобс', 'Исаксон', 610, 'бумага', 2128509, False)
cats_hause = Book('Кошкин дом', 'Маршак', 42, 'бумага', 2128510, False)

>>>>>>> 6a9ebe5236ef470b04e4ceb6ebf59917d01dc7af
print(matematika_5_class.print())
print(geography.print())
print(history.print())
print(club_5_am.print())
print(idiot.print())
print(ispoved_huligana.print())
print(steve_jobs.print())
print(cats_hause.print())
