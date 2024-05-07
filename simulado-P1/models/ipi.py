from imposto import Imposto


class IPI(Imposto):
    def __init__(self, aliquota: float, tem_aliquota_adicional: bool):
        super().__init__(aliquota)
        self.__tem_aliquota_adicional = tem_aliquota_adicional

    @property
    def tem_aliquota_adicional(self):
        return self.__tem_aliquota_adicional

    def calcula_aliquota(self):
        if self.__tem_aliquota_adicional:
            ipi = super().aliquota + 0.1 * super().aliquota
            return ipi
