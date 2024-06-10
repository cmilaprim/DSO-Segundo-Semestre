from abstractElevador import AbstractElevador
from Exception.elevadorCheioException import ElevadorCheioException
from Exception.elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from Exception.elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from Exception.elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andar_atual: int, total_andares_predio: int, capacidade: int, total_pessoas: int):
        self.__capacidade = capacidade
        self.__total_andares_predio = total_andares_predio
        self.__andar_atual = andar_atual
        self.__total_pessoas = total_pessoas
    
    def descer(self) -> str:
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            raise ElevadorJahNoTerreoException
    
    def entra_pessoa(self) -> str:
        if self.__total_pessoas < self.__capacidade:
            self.__total_pessoas += 1
        else:
            raise ElevadorCheioException
    
    def sai_pessoa(self) -> str:
        if self.__total_pessoas > 0:
            self.__total_pessoas -= 1
        else:
            raise ElevadorJahVazioException
    
    def subir(self) -> str:
        if self.__andar_atual < self.__total_andares_predio:
            self.__andar_atual += 1
        else:
            raise ElevadorJahNoUltimoAndarException

    
    @property
    def capacidade(self) -> int:
        return self.__capacidade
    
    @property
    def total_pessoas(self) -> int:
        return self.__total_pessoas
    
    @property
    def total_andares_predio(self) -> int:
        return self.__total_andares_predio
    
    @property
    def andar_atual(self) -> int:
        return self.__andar_atual