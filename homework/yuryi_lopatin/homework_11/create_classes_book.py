
class Book():
    material = 'paper'
    have_text = True

    def __init__(self, title, author, pages, book_type, reserve):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_type = book_type
        self.reserve = reserve

    def isbn(self):
        return self.isbn_number

    def print(self):
        if self.reserve:
            return (f'Название: {self.title}, Автор: {self.author}, страниц {self.pages}:, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}')

class SchoolBook(Book):
    def __init__(self, title, author, pages, book_type, reserve, subject, school_class, homework):
        super().__init__(title, author, pages, book_type, reserve)
        self.subject = subject
        self.school_class = school_class
        self.homework = homework

    def print(self):
        if self.homework:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject}')

matematika_5_class = SchoolBook('Matematika 5 class', 'Gipakra', 211, 'school book', True, 'Matematika', '5 class', True)
geogerphy = SchoolBook('Geopraphy 7 class', 'Christophor Columb', 240, 'school book', False, 'Matematika', '7 class', False)
history = SchoolBook('History 3 class', 'Isac Son', 210, 'school book',False, 'Matematika', '9 class', False)

club_5_am = Book('Club_5_am', 'Robin Sharma', 511, 'psyhology', True)
idiot = Book('Idiot', 'Dostoyevski', 640, 'fiction', False)
ispoved_huligana = Book('Ispoved Huligana', 'Esenin', 320, 'poetry',
                       False)
steve_jobs = Book('Steve Jobs', 'Issaacson', 610, 'biography',
                  False)
cats_hause = Book('Steve Jobs', 'Issaacson', 42, 'biography', False)

print(matematika_5_class.__dict__)
print(geogerphy.__dict__)
print(history.__dict__)
print(club_5_am.__dict__)
print(idiot.__dict__)
print(ispoved_huligana.__dict__)
print(steve_jobs.__dict__)
print(cats_hause.__dict__)
