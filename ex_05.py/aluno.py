from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU

class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    def emprestar(self, titulo_livro: str):
        return 'Aluno de matricula ' + '"' + str(self.matricula) + '"' + super().emprestar(titulo_livro)
    
    def devolver(self, titulo_livro: str):
        return 'Aluno de matricula "' + str(self.matricula) + super().devolver(titulo_livro)