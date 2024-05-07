from imposto import Imposto


class ISS(Imposto):
    def __init__(self, aliquota):
        super().__init__(aliquota)
        self.__servicos = []

    @property
    def servicos(self):
        return self.__servicos

    def inclui_servico(self, nome):
        if nome not in self.__servicos:
            self.__servicos.append(nome)

    def exclui_servico(self, nome):
        self.__servicos.remove(nome)

    def calcula_aliquota(self):
        iss = super().aliquota - (0.1 * (len(self.__servicos)))
        return iss
