class Endereco:
    
    def __init__(self, cidade: str='', estado: str=''):
        self.__cidade = cidade
        self.__estado = estado
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado 
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

class Aluno:
    
    def __init__(self, nome, cidade, estado):
        self.__nome = nome
        self.__endereco = Endereco(cidade, estado)
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

        
class Professor:
    
    def __init__(self, nome,cidade, estado, orientando: Aluno):
        self.__nome = nome
        self.__endereco = Endereco(cidade, estado)
        if isinstance(orientando, Aluno):
            self.__orientando = orientando

    
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, cidade, estado):
        self.__endereco = Endereco(cidade, estado)
        
    @property
    def orientando(self):
        return self.__orientando
    
    @orientando.setter
    def orientando(self, orientando):
        if isinstance(orientando, Aluno):
            self.__orientando = orientando
        
    

alunx = Aluno('camila', 'biguacu', 'santa catarina')
print(alunx.endereco.cidade)
print(alunx.endereco.estado)