
class Aluno:
    
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        
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
    
    def __init__(self, nome, endereco, orientando: Aluno):
        if isinstance(orientando, Aluno):
            self.__orientando = orientando
        self.__nome = nome
        self.__endereco = endereco
    
            
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
        
    @property
    def orientando(self):
        return self.__orientando
    
    @orientando.setter
    def orientando(self, orientando):
        if isinstance(orientando, Aluno):
            self.__orientando = orientando
        
    
#alunx = Aluno('camila', 'rua da camila')
#print(alunx.endereco)
#prof = Professor('Eduardo', 'Rua do Eduardo', alunx)
#print(prof.orientando)
#print(prof.orientando.nome)
#alunx.nome = 'Eduardinho'
#print(alunx.nome)

