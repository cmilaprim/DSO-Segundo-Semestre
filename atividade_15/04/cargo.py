class Cargo:
    
    def __init__(self, salario: int, descricao: str):
        self.__salario = salario
        self.__descricao = descricao

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        