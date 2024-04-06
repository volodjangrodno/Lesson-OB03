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

author = Author('J.K. Rowling', 'British')
book = Book('Harry Potter', author)

print(f"Книга : {book.title}, Автор: {book.author.name}, Национальность автора: {book.author.nationality}")