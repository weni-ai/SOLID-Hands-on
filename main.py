from attendants import Attendant
from books import Book
from clients import Client

def main():
    Book('Teste 1', 'Teste desc 1', '50', 'Adult', 1)
    Book('Teste 2', 'Teste desc 2', '500', 'Adventure', 2)
    Book.list_books()
    Client('Eduardo', '123456', '27', '9292929', 'a@a.com', 1)
    Client.list_clients()
    Attendant('Nicácio', '321321', '23', '999999', 'b@b.com', '1500', 1)
    Attendant.list_attendants()


if __name__ == "__main__":
    main()
