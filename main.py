import uuid
from dataclasses import dataclass
from enum import Enum
from abc import ABCMeta, abstractmethod

#Pseudo Database
class Database(metaclass=ABCMeta):

    BOOKS = []
    CLIENTS = []
    ATTENDANTS = []
    GETTED_BOOKS = []

    @abstractmethod
    def create(self):
        raise NotImplementedError

#Enums
class BookGender(Enum):
    ROMANCE = 'Romance'
    DRAMA = 'Drama'
    FICTION = 'Fiction'
    FANTASY = 'Fantasy'
    OTHER = 'Other'


#Data
@dataclass
class Book(Database):
    title: str
    description: str
    pages: int
    gender: BookGender
    id: str = uuid.uuid4().hex

    def create(self):
        self.BOOKS.append(self)
        print(f"[ * ] adding: {self}")

    def rent(self):
        self.GETTED_BOOKS.append(self)
        print(f"[ * ] adding: {self}")

@dataclass
class Client(Database):
    name: str
    cpf: str
    age: int
    cell_number: str
    email: str
    id: str = uuid.uuid4().hex
    
    def create(self):
        self.CLIENTS.append(self)
        print(f"[ * ] adding: {self}")

@dataclass
class Attendant(Database):
    name:str
    cpf: str
    age: int
    cell_number: str
    email: str
    salary: float
    id: str = uuid.uuid4().hex

    def create(self):
        self.ATTENDANTS.append(self)
        print(f"[ * ] adding: {self}")

def main():
    pass

    # Example of creating and renting a book
    # book1 = Book(title='Book1', description='Book', pages=10, gender=BookGender.FANTASY)
    # book1.create()
    # book1.rent()


if __name__ == "__main__":
    main()