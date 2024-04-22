from funcionario import Funcionario

class Administrativo(Funcionario):
    
    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, dias_de_emprestimo = 10)
        self.dias_de_emprestimo = str(10)

    
    def emprestar(self, titulo_livro: str):
        return 'Administrativo ' + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return 'Administrativo ' + super().devolver(titulo_livro)

p1 = Administrativo("CTC", 15615)
print(p1.emprestar("Love"))