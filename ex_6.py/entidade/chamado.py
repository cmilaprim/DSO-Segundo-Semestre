from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(self, data: Date, cliente: Cliente, tecnico: Tecnico,
                titulo: str, descricao: str, prioridade: int,tipo: TipoChamado):
        if (isinstance(data, Date)):
            self.__data = data
        if (isinstance(cliente, Cliente)):
            self.__cliente = cliente
        if (isinstance(tecnico, Tecnico)):
            self.__tecnico = tecnico
        if (isinstance(titulo, str)):
            self.__titulo = titulo
        if (isinstance(descricao, str)):
            self.__descricao = descricao
        if (isinstance(prioridade, int)):
            self.__prioridade = prioridade
        if (isinstance(tipo, TipoChamado)):
            self.__tipo = tipo

    @property
    def data(self) -> Date:
        return self.__data
    
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
    
    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @property
    def prioridade(self) -> int:
        return self.__prioridade
    
    @property
    def tipo(self) -> TipoChamado:
        return self.__tipo

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
    
    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
    
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
    
    @prioridade.setter
    def prioridade(self, prioridade: int):
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
    
    @tipo.setter
    def tipo(self, tipo: TipoChamado):
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo
