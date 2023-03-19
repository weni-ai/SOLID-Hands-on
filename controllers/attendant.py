from usecases.dto.dtoAttendant import DTOAttendant
from usecases.attendant.create import CreateAttendant
from usecases.attendant.delete import DeleteAttendant
from usecases.attendant.update import UpdateAttendant
from usecases.attendant.read import ReadAttendant

class TestingUseCasesAttendant():
    def __init__(self) -> None:        
        infoAttend = DTOAttendant(
            "Helio Silva",
            "000000000000",
            35, 
            "558200000000",
            "tsi.heliosilva@gmail.com",
            25,
            1);
        CreateAttendant(infoAttend)
        ReadAttendant(infoAttend.id)
        UpdateAttendant(infoAttend)
        DeleteAttendant(infoAttend.id)
        