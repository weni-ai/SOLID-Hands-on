from entities.client import Client

class DeleteClient():
    def __init__(self,id: int):
        print("\n")
        print("Use case: DeleteClient ( Validations )")
        client = Client()
        client.delete(id)
        print("\n")
