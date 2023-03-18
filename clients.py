from databases import Database

class Client(Database):
    def __init__(self, name, cpf, age, cell_number, email, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.id = id
        self.create()
    
    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email)

    def create(self):
        self.clients.append(self)
        print(f'[ * ] adding {self.name}')
    
    @staticmethod
    def list_clients():
        for client in Client.clients:
            print(client)

    def __repr__(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}"
