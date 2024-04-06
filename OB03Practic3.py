# Задача №3.
#
# Создайте класс Author и класс Book.
# Класс Book должен использовать композицию для включения автора в качестве объекта.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info_book(self):
        print(f"Книга : {self.title}, Автор: {self.author.name}, Национальность автора: {self.author.nationality}")

author = Author('J.K. Rowling', 'British')
book = Book('Harry Potter', author)

book.info_book()