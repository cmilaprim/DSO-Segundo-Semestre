from imposto import Imposto


class IPI(Imposto):
    def __init__(self, aliquota, tem_aliquota_adicional: bool):
        self.__aliquota = aliquota
        self.__tem_aliquota_adicional = tem_aliquota_adicional

    def calcula_aliquota(self):
        if self.__tem_aliquota_adicional:
            ipi = self.__aliquota + 0.1 * self.__aliquota
            return ipi
        return

    @property
    def aliquota(self):
        return self.__aliquota
