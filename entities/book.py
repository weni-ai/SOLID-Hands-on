from entities.database import Database

class Book(Database):           

    def create(self,  title, description, pages, gender, id):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender
        self.id = id
        print("Saving in database...")
        return 

    def findByOneOrDefault(self, id: int):
        self.title = "Book found in database exemple"
        self.description = "Clean architecture application"
        self.gender = "Tech"
        self.pages = 1
        self.id = id
        print("Find by id or return default(null)...")
        return self
    
    def update(self, title, description, pages, gender):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender
        print("Updating in database ")
        return
    
    def delete(self, id):
        foundBook = self.findByOneOrDefault(id)
        if foundBook:
          print("Deleting in database ")
        return

    def to_json(self):
        return dict(title=self.title, description=self.description, pages=self.pages, gender=self.gender)

    def to_str(self):
        return f"title: {self.title}, description: {self.description}, pages: {self.pages}, gender: {self.gender}"
