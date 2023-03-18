from abc import ABCMeta, abstractmethod

class Database(metaclass=ABCMeta):
    books = []
    clients = []
    attendants = []
    getted_books = []

    @abstractmethod
    def create(self):
        pass
