from funcionario import Funcionario

class Administrativo(Funcionario):
    
    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, dias_de_emprestimo = 10)
        self.dias_de_emprestimo = str(10)

    
    def emprestar(self, titulo_livro: str):
        return 'Funcionario administrativo do departamento "' + self.departamento + '" pegou emprestado o livro: ' + titulo_livro + ' com ' + str(self.dias_de_emprestimo) + " dias de prazo"

    def devolver(self, titulo_livro: str):
        return 'Funcionario administrativo do departamento "' + self.departamento  + '" devolveu o livro: ' + titulo_livro

