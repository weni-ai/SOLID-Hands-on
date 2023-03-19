from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findByOneOrDefault(self, id: int):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    # def rent_book(self, id_book, id_client, id_attendant, price, type):
    #     self.getted_books.append(
    #         dict(
    #             id_book=id_book,
    #             id_attendant=id_attendant,
    #             id_client=id_client,
    #             price=price,
    #             type=type
    #         )
    #     )