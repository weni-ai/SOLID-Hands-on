from entities.book import Book

class DeleteBook():
    def __init__(self,id: int):
        print("\n")
        print("Use case: DeleteBook ( Validations )")
        book = Book()
        book.delete(id)
        print("\n")
