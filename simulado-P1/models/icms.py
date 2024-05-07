from imposto import Imposto


class ICMS(Imposto):
    def __init__(self, aliquota, diferenca_estado):
        super().__init__(aliquota)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado):
        if isinstance(diferenca_estado, float):
            self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self):
        icms = super().aliquota + self.__diferenca_estado
        return icms
