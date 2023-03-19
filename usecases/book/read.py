from entities.book import Book

class ReadBook():
    def __init__(self,id: int) -> Book:
        print("\n")
        print("Use case: ReadBook ( Validations )")
        book = Book()
        foundBook = book.findByOneOrDefault(id)
        print(foundBook.to_str)
        print("\n")
