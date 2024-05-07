from imposto import Imposto


class ICMS(Imposto):
    def __init__(self, aliquota: float, diferenca_estado: float):
        super().__init__(aliquota)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    def calcula_aliquota(self):
        icms = super().aliquota + self.__diferenca_estado
        return icms
