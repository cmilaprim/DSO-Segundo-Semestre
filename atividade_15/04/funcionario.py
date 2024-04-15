from pessoa import Pessoa
from dependente import Dependente
from cargo import Cargo

class Funcinario(Pessoa):
    
    def __init__(self, nome: str, cpf: str, cargo: Cargo):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__dependentes = []
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
    
    @property
    def dependentes(self):
        return self.__dependentes

    @dependentes.setter
    def dependentes(self, depedentes):
        self.__dependentes = depedentes
    
    def add_dependente(self, nome,cpf):
        dependente = Dependente(nome, cpf)
        for dep in self.__dependentes:
            if dep.cpf == cpf:
                print("Erro")
                return None
        self.__dependentes.append(dependente)


    def rem_depentende(self,cpf):
        for depentende in self.__dependentes:
            if depentende.cpf == cpf:
                self.dependentes.remove(depentende)
    
    def mostra_dados(self):
        print(f"Nome: {self.nome}\nCARGO: {self.cargo}\nCPF: {self.cpf}" )

f1 = Funcinario("Camila", "5484860", "TI")
f1.mostra_dados()