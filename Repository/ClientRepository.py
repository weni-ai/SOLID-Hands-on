import CRUDInterface
from Domain import Client, Book, Attendant

class ClientRepository(CRUDInterface):

    clients = list()

    def create(self, client: Client):
        self.clients.append(client)
        print(f'[ * ] adding {client.name}')
    def update(self, client: Client):
        # TODO
        pass
    def get(self, client: Client):
        # TODO
        pass
    def delete(self, client: Client):
        # TODO
        pass     
    def rentBooks(self, client:Client, book: Book, attendant: Attendant):
        dict(
                id_book=id_book,
                id_attendant=id_attendant,
                id_client=id_client,
                price=price,
                type=type
            )
        client.getted_books.append(book)

        