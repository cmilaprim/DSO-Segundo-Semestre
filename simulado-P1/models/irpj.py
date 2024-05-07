from imposto import Imposto


class IRPJ(Imposto):
    def __init__(self, aliquota: float, desconto: float):
        super().__init__(aliquota)
        self.__desconto = desconto

    @property
    def desconto(self):
        return self.__desconto

    def calcula_aliquota(self):
        irpj = super().aliquita - self.__desconto
        return irpj
