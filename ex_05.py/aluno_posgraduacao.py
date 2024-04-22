from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
    
    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    
    @elaborando_tese.setter
    def elaborando_tese(self,elaborando_tese):
        self.__elaborando_tese = elaborando_tese
    
    def emprestar(self, titulo_livro: str):
        if self.elaborando_tese == True:
            self.dias_de_emprestimo = str(self.dias_de_emprestimo * 2)
            return super().emprestar(titulo_livro)     

    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)

a1 = AlunoPosGraduacao(44845, 20, 1455445)
a1.elaborando_tese = True
print(a1.emprestar("paz"))