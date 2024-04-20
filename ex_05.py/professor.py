from funcionario import Funcionario

class Professor(Funcionario):
    
    def __init__(self, departamento: str, cpf: int, ):
        super().__init__(departamento, cpf, dias_de_emprestimo = 20)
        self.dias_de_emprestimo = str(20)
    
    def emprestar(self, titulo_livro: str):
        return 'Professor do departamento "' + self.departamento + '" pegou emprestado o livro: ' + titulo_livro + ' com ' + str(self.dias_de_emprestimo) + " dias de prazo"

    def devolver(self, titulo_livro: str):
        return 'Professor do departamento "' + self.departamento  + '" devolveu o livro: ' + titulo_livro

p1 = Professor("CTC", 15615)
print(p1.emprestar("Love"))