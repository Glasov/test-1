cat > iterator.py << 'EOF'
class BookCollection:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __iter__(self):
        return BookIterator(self.books)

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

# Пример
if __name__ == "__main__":
    library = BookCollection()
    library.add_book("Война и мир")
    library.add_book("Преступление и наказание")
    
    for book in library:
        print(f"Книга: {book}")
EOF