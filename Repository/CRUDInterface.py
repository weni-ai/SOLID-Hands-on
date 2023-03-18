from abc import ABCMeta, abstractmethod

class CRUDInterface(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def delete(self):
        pass