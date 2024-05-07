from imposto import Imposto


class IRPJ(Imposto):
    def __init__(self, aliquota, desconto: float):
        super().__init__(aliquota)
        self.__desconto = desconto

    def calcula_aliquota(self):
        irpj = super().aliquota - self.__desconto
        return irpj
