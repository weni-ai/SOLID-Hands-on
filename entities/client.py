from entities.database import Database

class Client(Database):           

    def create(self, name, cpf, age, cell_number, email, id):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.id = id
        print("Saving in database...")
        return 

    def findByOneOrDefault(self, id: int):
        self.name = "Helio Silva"
        self.cpf = "00000000000"
        self.age = 35
        self.cell_number = "+55 82 99613-0940"
        self.email = "tsi.heliosilva@gmail.com"
        self.id = id
        print("Find by id or return default(null)...")
        return self
    
    def update(self, name, cpf, age, cell_number, email,):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.cell_number = cell_number
        self.email = email
        self.id = id
        print("Updating in database ")
        return
    
    def delete(self, id):
        foundClient = self.findByOneOrDefault(id)
        if foundClient:
          print("Deleting in database ")
        return

    def to_json(self):
        return dict(name=self.name, cpf=self.cpf, age=self.age, cell_number=self.cell_number, email=self.email)

    def to_str(self):
        return f"name: {self.name}, cpf: {self.cpf}, age: {self.age}, cell_number: {self.cell_number}, email: {self.email}"
