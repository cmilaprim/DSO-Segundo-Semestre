class Capitulo:
    
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo =  titulo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero:int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def nome(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

