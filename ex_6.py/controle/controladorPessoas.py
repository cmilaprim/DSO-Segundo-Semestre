from abstractControladorPessoas import AbstractControladorPessoas
from entidade.cliente import Cliente
from entidade.tecnico import Tecnico

class ControladorPessoas(AbstractControladorPessoas):
    
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self) -> list:
        return self.__clientes
    
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        novo_cliente = Cliente(nome, codigo)
        for cliente in self.__clientes:
            if cliente.codigo == novo_cliente.codigo:
                return None 
            else:
                self.__clientes.append(novo_cliente)
        return novo_cliente
    
    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        novo_tecnico = Tecnico(nome, codigo)
        for tecnico in self.__tecnicos:
            if tecnico.nome == novo_tecnico.nome:
                return None
            else:
                self.__tecnicos.append(novo_tecnico)
        return novo_tecnico

