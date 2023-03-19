from controllers.book import TestingUseCasesBook
from controllers.client import TestingUseCasesClient
from controllers.attendant import TestingUseCasesAttendant

def main():
    print("Usecases Books")
    TestingUseCasesBook()
    print("Usecases Clients")
    TestingUseCasesClient()
    print("Usecases Attendants")
    TestingUseCasesAttendant()


if __name__ == "__main__":
    main()
