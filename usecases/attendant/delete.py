from entities.attendant import Attendant

class DeleteAttendant():
    def __init__(self,id: int):
        print("\n")
        print("Use case: DeleteAttendant ( Validations )")
        attend = Attendant()
        attend.delete(id)
        print("\n")
