from imposto import Imposto


class ISS(Imposto):

    def __init__(self, aliquota: float):
        super().__init__(aliquota)
        self.__servicos = []

    def inclui_servio(self, nome):
        if nome not in self.__servicos:
            self.__servicos.append(nome)

    def exlcui_servico(self, nome):
        self.__servicos.remove(nome)

    def calcula_aliquota(self):
        iss = super().aliquota - (0.1 * (len(self.__servicos)))
        return iss
