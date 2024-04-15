from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):        
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.__autores.append(autor)
        self.__capitulos = []
        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos.append(capitulo)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo:int):
        if  isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo,str):
            self.__titulo = titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autores
    
    @property
    def autores(self):
        return self.__autores
    
    @property
    def capitulos(self):
        return self.__capitulos
    
    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)
        return None

    def excluir_autor(self, autor:Autor):
        if (isinstance(autor, Autor)):
            self.__autores.remove(autor)
        return None

    def incluir_capitulo(self, numero_capitulo: int, titulo_capitulo: str):
        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        if capitulo not in self.__capitulos:
            self.__capitulos.append(capitulo)
        return None

    def excluir_capitulo(self, titulo:str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                self.__capitulos.remove(capitulo)
        return None

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
            else:
                return None