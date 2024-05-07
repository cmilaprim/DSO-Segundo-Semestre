from imposto import Imposto
from ipi import IPI
from icms import ICMS
from iss import ISS


class Empresa:
    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cpnj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.0
        self.__faturamento_producao = 0.0
        self.__faturamento_vendas = 0.0

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia):
        if isinstance(nome_de_fantasia, str):
            self.__nome_de_fantasia = nome_de_fantasia

    @property
    def impostos(self):
        return self.__impostos

    @property
    def cnpj(self):
        return self.__cpnj

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    def inclui_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto):
            if imposto not in self.__impostos:
                self.__impostos.append(imposto)

    def remove_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto):
            if imposto in self.__impostos:
                self.__impostos.remove(imposto)

    def faturamento_total(self) -> float:
        faturamento_total = self.__faturamento_producao +\
            self.__faturamento_servicos + self.__faturamento_vendas
        return faturamento_total

    def total_impostos(self) -> float:
        imposto_total = 0.0
        for imposto in self.__impostos:
            if isinstance(imposto, IPI):
                imposto_total += (imposto.calcula_aliquota() / 100) * \
                    self.__faturamento_producao
            elif isinstance(imposto, ICMS):
                imposto_total += (imposto.calcula_aliquota() / 100) * \
                    self.__faturamento_vendas
            elif isinstance(imposto, ISS):
                imposto_total += (imposto.calcula_aliquota() / 100) * \
                    self.__faturamento_servicos
            else:
                imposto_total += (imposto.calcula_aliquota() / 100) * \
                    self.faturamento_total()
        return imposto_total

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        self.__faturamento_producao = fat_producao
        self.__faturamento_servicos = fat_servicos
        self.__faturamento_vendas = fat_vendas
