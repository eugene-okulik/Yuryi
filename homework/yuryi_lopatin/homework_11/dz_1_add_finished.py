from abc import abstractmethod
from tokenize import group


class Book():
    have_text = True

    def __init__(self, title, author, pages, material, book_type, reserve):
        self.title = title
        self.author = author
        self.pages = pages
        self.material = material
        self.book_type = book_type
        self.reserve = reserve

    def isbn(self):
        return self.isbn_number

    def print(self):
        if self.reserve:
            return (f'Название: {self.title}, Автор: {self.author}, страниц {self.pages}:, '
                    f'материал: {self.material}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                    f'материал: {self.material}')


class SchoolBook(Book):

    def __init__(self, title, author, pages, material, book_type, reserve, subject, group, homework):
        super().__init__(title, author, pages, material, book_type, reserve)
        self.subject = subject
        self.group = group
        self.homework = homework

    def print(self):
        if self.homework:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject}')


matematika_5_class = SchoolBook('Matematika 5 class', 'Gipakra', 211, 'paper',
                                'school book', True, 'Matematika', '5 class',
                                True)
geogerphi = SchoolBook('Geopraphy 7 class', 'Christophor Columb', 240, 'paper',
                       'school book', False, 'Matematika', '7 class', False)
history = SchoolBook('History 3 class', 'Isac Son', 210, 'paper',
                     'school book',False, 'Matematika', '9 class', False)

club_5_am = Book('Club_5_am', 'Robin Sharma', 511, 'paper', 'psyhology',
                 True)
idiot = Book('Idiot', 'Dostoyevski', 640, 'paper', 'fiction', False)
ispovedhuligana = Book('Ispoved Huligana', 'Esenin', 320, 'paper','poetry',
                       False)
steve_jobs = Book('Steve Jobs', 'Issaacson', 610, 'paper', 'biography',
                  False)
cats_hause = Book('Steve Jobs', 'Issaacson', 610, 'paper', 'biography',
                  False)


print(matematika_5_class.__dict__)
print(geogerphi.__dict__)
print(history.__dict__)

print(club_5_am.__dict__)
print(idiot.__dict__)
print(ispovedhuligana.__dict__)
print(steve_jobs.__dict__)
print(cats_hause.__dict__)
