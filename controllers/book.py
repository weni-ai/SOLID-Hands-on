from usecases.dto.dtoBook import DTOBook
from usecases.book.create import CreateBook
from usecases.book.delete import DeleteBook
from usecases.book.update import UpdateBook
from usecases.book.read import ReadBook

class TestingUseCasesBook():
    def __init__(self) -> None:        
        infoLivro = DTOBook(
            "A procura da felicidade",
            "Livro motivacional",
            1250, 
            "Clássico",
            1);
        CreateBook(infoLivro)
        ReadBook(infoLivro.id)
        UpdateBook(infoLivro)
        DeleteBook(infoLivro.id)
        