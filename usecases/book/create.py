from entities.book import Book
from usecases.dto.dtoBook import DTOBook

class CreateBook():
    def __init__(self,dtoBook: DTOBook) -> Book:
        print("\n")
        print("Use case: CreateBook ( Validations )")
        book = Book()
        book.create(dtoBook.title,dtoBook.description,dtoBook.pages,dtoBook.gender,dtoBook.id)
        print("\n")