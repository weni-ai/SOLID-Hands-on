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


class Client:
    def __init__(self, name, cpf, age, cell_number, email, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.id = id
    
    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}"


class Attendant:
    def __init__(self, name, cpf, age, cell_number, email, salary, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.salary = salary
        self.id = id

    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email, salary=self.salary)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}, salary: {self.salary}"


class Database:

    books = []
    clients = []
    attendants = []
    getted_books = []

    def create_client(self, client):
        self.clients.append(client)
        print(f'[ * ] adding {client.name}')

    def create_book(self, book):
        self.books.append(book)
        print(f"[ * ] adding {book.title}")

    def create_attendenant(self, attendant):
        self.attendants.append(attendant)
        print(f"[ * ] adding {attendant.name}")
    
    def rent_book(self, id_book, id_client, id_attendant, price, type):
        self.getted_books.append(
            dict(
                id_book=id_book,
                id_attendant=id_attendant,
                id_client=id_client,
                price=price,
                type=type
            )
        )

def main():
    pass


if __name__ == "__main__":
    main()
