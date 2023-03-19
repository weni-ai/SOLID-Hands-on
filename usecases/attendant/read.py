from entities.attendant import Attendant

class ReadAttendant():
    def __init__(self,id: int) -> Attendant:
        print("\n")
        print("Use case: ReadAttendant ( Validations )")
        attend = Attendant()
        attend = attend.findByOneOrDefault(id)
        print(attend.to_str)
        print("\n")
