from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
    
    @abstractmethod
    def mostra_dados(self):
        print(f"Nome: {self.nome}\nCPF: {self.__cpf}")
        #OU DEIXAR UM PASS NA FORMA MAIS SIMPLES POSSIVEL 