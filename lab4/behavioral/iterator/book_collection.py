"""
Паттерн Итератор (Iterator)
Предоставляет способ последовательного доступа к элементам
составного объекта без раскрытия его внутреннего представления.
"""

from collections.abc import Iterator, Iterable
from typing import List

# Книга
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' - {self.author}"

# Итератор для книг
class BookIterator(Iterator):
    def __init__(self, books: List[Book], reverse: bool = False):
        self.books = books
        self.reverse = reverse
        self.index = len(books) - 1 if reverse else 0
    
    def __next__(self):
        try:
            book = self.books[self.index]
            if self.reverse:
                self.index -= 1
            else:
                self.index += 1
            return book
        except IndexError:
            raise StopIteration()

# Коллекция книг
class BookCollection(Iterable):
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def __iter__(self) -> BookIterator:
        return BookIterator(self.books)
    
    def get_reverse_iterator(self) -> BookIterator:
        return BookIterator(self.books, reverse=True)
