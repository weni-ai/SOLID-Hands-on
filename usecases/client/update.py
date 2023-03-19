from entities.client import Client
from usecases.dto.dtoClient import DTOClient

class UpdateClient():
    def __init__(self,dtoClient: DTOClient) -> Client:
        print("\n")
        print("Use case: UpdateClient ( Validations )")
        client = Client()
        foundClient = client.findByOneOrDefault(dtoClient.id)
        if foundClient:
            client.update(dtoClient.name,dtoClient.cpf,dtoClient.age,dtoClient.cell_number,dtoClient.email)
        print("\n")