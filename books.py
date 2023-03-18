from databases import Database


class Book(Database):
    def __init__(self, title, description, pages, gender, id):
        self.title = title
        self.description = description
        self.pages = pages
        self.gender = gender
        self.id = id
        self.create()

    def to_json(self):
        return dict(title=self.title, description=self.description, pages=self.pages, gender=self.gender)
    
    def create(self):
        self.books.append(self)
        print(f"[ * ] adding {self.title}")
    
    def rent_book(self):
        self.getted_books.append(
            dict(
                id_book=self.id_book,
                id_attendant=self.id_attendant,
                id_client=self.id_client,
                price=self.price,
                type=self.type
            )
        )
    
    @staticmethod
    def list_books():
        for book in Book.books:
            print(book)

    def __repr__(self):
        return f"title: {self.title}, description: {self.description}, pages: {self.pages}, gender: {self.gender}"
