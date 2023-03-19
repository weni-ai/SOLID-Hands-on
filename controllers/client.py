from usecases.dto.dtoClient import DTOClient
from usecases.client.create import CreateClient
from usecases.client.delete import DeleteClient
from usecases.client.update import UpdateClient
from usecases.client.read import ReadClient

class TestingUseCasesClient():
    def __init__(self) -> None:        
        infoClient = DTOClient(
            "Helio Silva",
            "000000000000",
            35, 
            "558200000000",
            "tsi.heliosilva@gmail.com",
            1);
        CreateClient(infoClient)
        ReadClient(infoClient.id)
        UpdateClient(infoClient)
        DeleteClient(infoClient.id)
        