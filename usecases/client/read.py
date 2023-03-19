from entities.client import Client

class ReadClient():
    def __init__(self,id: int) -> Client:
        print("\n")
        print("Use case: ReadClient ( Validations )")
        client = Client()
        foundClient = client.findByOneOrDefault(id)
        print(foundClient.to_str)
        print("\n")
