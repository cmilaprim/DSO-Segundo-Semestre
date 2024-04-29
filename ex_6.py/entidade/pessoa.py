from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa

class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
