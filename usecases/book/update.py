from entities.book import Book
from usecases.dto.dtoBook import DTOBook

class UpdateBook():
    def __init__(self,dtoBook: DTOBook) -> Book:
        print("\n")
        print("Use case: UpdateBook ( Validations )")
        book = Book()
        foundBook = book.findByOneOrDefault(dtoBook.id)
        if foundBook:
            book.update(dtoBook.title,dtoBook.description,dtoBook.pages,dtoBook.gender)
        print("\n")