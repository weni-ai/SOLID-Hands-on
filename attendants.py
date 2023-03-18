from databases import Database

class Attendant(Database):
    def __init__(self, name, cpf, age, cell_number, email, salary, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.salary = salary
        self.id = id
        self.create()

    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email, salary=self.salary)

    def create(self):
        self.attendants.append(self)
        print(f"[ * ] adding {self.name}")

    @staticmethod
    def list_attendants():
        for attendant in Attendant.attendants:
            print(attendant)

    def __repr__(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}, salary: {self.salary}"
