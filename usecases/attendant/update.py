from entities.attendant import Attendant
from usecases.dto.dtoAttendant import DTOAttendant

class UpdateAttendant():
    def __init__(self,dtoAttend: DTOAttendant) -> Attendant:
        print("\n")
        print("Use case: UpdateAttendant ( Validations )")
        attend = Attendant()
        attend = attend.findByOneOrDefault(dtoAttend.id)
        if attend:
            attend.update(dtoAttend.name,dtoAttend.cpf,dtoAttend.age,dtoAttend.cell_number,dtoAttend.email, dtoAttend.salary, dtoAttend.id)
        print("\n")