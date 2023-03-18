import CRUDInterface
import Domain.Book

class BookRepository(CRUDInterface):

    books = list()

    def create(self, book: Domain.Book):
        self.books.append(book)
        print(f'[ * ] adding {attendant.name}')
    def update(self, book: Domain.Book):
        # TODO
        pass
    def get(self, book: Domain.Book):
        # TODO
        pass
    def delete(self, book: Domain.Book):
        # TODO
        pass     
