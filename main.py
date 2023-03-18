from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, cpf, age, cell_number, email, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.id = id

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def to_str(self):
        pass


class Book:
    def __init__(self, title, description, pages, gender, id):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender
        self.id = id

    def to_json(self):
        return dict(title=self.title, description=self.description, pages=self.pages, gender=self.gender)

    def to_str(self):
        return f"title: {self.title}, description: {self.description}, pages: {self.pages}, gender: {self.gender}"


class Client(Person):
    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}"


class Attendant(Person):
    def __init__(self, name, cpf, age, cell_number, email, salary, id):
        super().__init__(name, cpf, age, cell_number, email, id)
        self.salary = salary

    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email, salary=self.salary)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}, salary: {self.salary}"


class IRepository(ABC):
    @abstractmethod
    def create(self, obj):
        pass


class BookRepository(IRepository):
    books = []

    def create(self, book):
        self.books.append(book)
        print(f"[ * ] adding {book.title}")


class ClientRepository(IRepository):
    clients = []

    def create(self, client):
        self.clients.append(client)
        print(f'[ * ] adding {client.name}')


class AttendantRepository(IRepository):
    attendants = []

    def create(self, attendant):
        self.attendants.append(attendant)
        print(f"[ * ] adding {attendant.name}")


class Rent:
    def __init__(self, id_book, id_client, id_attendant, price, type_of_rent):
        self.id_book = id_book
        self.id_client = id_client
        self.id_attendant = id_attendant
        self.price = price
        self.type_of_rent = type_of_rent


class RentRepository(IRepository):
    rented_books = []

    def create(self, rent):
        self.rented_books.append(rent)


def main():
    # TESTING THE CODE
    # Creating instances of repositories
    book_repository = BookRepository()
    client_repository = ClientRepository()
    attendant_repository = AttendantRepository()
    rent_repository = RentRepository()

    # Creating a book, client, and attendant
    book = Book("Livro 1", "Exemplo de livro 1 com código refatorado para SOLID", 200, "Fiction", 1)
    client = Client("Fulano de Tal", "123.456.789-00", 25, "555-1234", "fuladodetal@gmail.com", 1)
    attendant = Attendant("Ciclana da Silva", "987.654.321-00", 30, "555-5678", "ciclanadasilva@gmail.com", 2500, 1)

    # Adding book, client, and attendant to their respective repositories
    book_repository.create(book)
    client_repository.create(client)
    attendant_repository.create(attendant)

    # Renting a book
    rent = Rent(book.id, client.id, attendant.id, 20, "Regular")
    rent_repository.create(rent)

    # Example of using to_json() and to_str() methods
    print()
    print(book.to_json())
    print(book.to_str())

    print()
    print(client.to_json())
    print(client.to_str())

    print()
    print(attendant.to_json())
    print(attendant.to_str())

    print()


if __name__ == "__main__":
    main()


