class Pessoa():
    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        
#p1 = Pessoa('camila')
#print(p1.nome)
#p1.nome = 'eduarda'
#print(p1.nome)

#p1 = Pessoa('joao', 21)
#p2 = Pessoa('joao', 21)
#print(p1 == p2)
#print(p1)
#print(p2)
#print(p1.nome == p2.nome)

