from entities.attendant import Attendant
from usecases.dto.dtoAttendant import DTOAttendant

class CreateAttendant():
    def __init__(self,dtoAttendant: DTOAttendant) -> Attendant:
        print("\n")
        print("Use case: CreateAttendant ( Validations )")
        attend = Attendant()
        attend.create(dtoAttendant.name,dtoAttendant.cpf,dtoAttendant.age,dtoAttendant.cell_number,dtoAttendant.email, dtoAttendant.salary, dtoAttendant.id)
        print("\n")