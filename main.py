class Database:
    books = []
    clients = []
    attendants = []
    getted_books = []
    

class Book(Database):
    def __init__(self, title: str, description: str, pages: int, gender: str, id: str):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender
        self.id = id

    def to_json(self):
        return dict(title=self.title, description=self.description, pages=self.pages, gender=self.gender)

    def to_str(self):
        return f"title: {self.title}, description: {self.description}, pages: {self.pages}, gender: {self.gender}"

    def create_book(self):
        super().books.append(self)
        print(f"[ * ] adding {self.title}")

    def rent_book(self, id_book, id_client, id_attendant, price, type):
        super().getted_books.append(
            dict(
                id_book=self.id_book,
                id_attendant=self.id_attendant,
                id_client=self.id_client,
                price=self.price,
                type=self.type
            )
        )

class Client(Database):
    def __init__(self, name: str, cpf: str, age: int, cell_number: int, email: str, id: str):
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

    def create_client(self):
        super().clients.append(self)
        print(f'[ * ] adding {self.name}')

class Attendant(Database):
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

    def create_attendenant(self):
        super().attendants.append(self)
        print(f"[ * ] adding {self.name}")


def main():
    pass


if __name__ == "__main__":
    main()
