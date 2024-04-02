class Cliente:
    
    def __init__(self,nome,fone):
        self.__nome = nome
        self.__fone = fone
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def fone(self):
        return self.__fone
    
    @nome.setter
    def nome(self,fone):
        self.__fone = fone
        

class CategoriaProduto:
    
    def __init__(self, titulo):
        self.__titulo = titulo
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def nome(self,titulo):
        self.__titulo = titulo
    
class Produto:
    
    def __init__(self, codigo, descricao, categoria_produto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = None 
        
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self,descricao):
        self.__nome = descricao
        
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def categoria_produto(self):
        return self.__categoria_produto
    
    @descricao.setter
    def categoria_produto(self, titulo):
        self.__categoria_produto = CategoriaProduto(titulo)
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
    
    
    def preco_total(self):
        self.__preco_total = self.__quantidade * self.__preco_unitario
        return self.__preco_total
    
        