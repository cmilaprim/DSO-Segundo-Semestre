from pessoa import Pessoa

class Dependente(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
    
    def mostra_dados(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}" )
        #DA PARA DEIXAR UM super().mostra_dados()

d1 = Dependente('Camila', "1575151584")
d1.mostra_dados()