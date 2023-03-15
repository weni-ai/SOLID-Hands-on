class Book:
    def __init__(self, title, description, pages, gender):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender

    def to_json(self):
        return dict(title=self.title, description=self.description, pages=self.pages, gender=self.gender)

    def to_str(self):
        return f"title: {self.title}, description: {self.description}, pages: {self.pages}, gender: {self.gender}"


class Client:
    def __init__(self, name, cpf, age, cell_number, email):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
    
    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}"


class Attendant:
    def __init__(self, name, cpf, age, cell_number, email, salary):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.salary = salary

    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email, salary=self.salary)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}, salary: {self.salary}"


class Database:

    books = []
    clients = []

    def create_client():
        pass

    def create_book():
        pass

    def create_attendenant():
        pass


def main():
    pass


if __name__ == "__main__":
    main()
