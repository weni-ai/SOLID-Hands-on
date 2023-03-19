from entities.client import Client
from usecases.dto.dtoClient import DTOClient

class CreateClient():
    def __init__(self,dtoClient: DTOClient) -> Client:
        print("\n")
        print("Use case: CreateClient ( Validations )")
        client = Client()
        client.create(dtoClient.name,dtoClient.cpf,dtoClient.age,dtoClient.cell_number,dtoClient.email,dtoClient.id)
        print("\n")