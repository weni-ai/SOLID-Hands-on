import CRUDInterface
import Domain.Attendant

class AttendantRepository(CRUDInterface):

    attendants = list()
    
    def create(self, attendant: Domain.Attendant):
        self.attendants.append(attendant)
        print(f'[ * ] adding {attendant.name}')
    def update(self, attendant: Domain.Attendant):
        # TODO
        pass
    def get(self, attendant: Domain.Attendant):
        # TODO
        pass
    def delete(self, attendant: Domain.Attendant):
        # TODO
        pass     
