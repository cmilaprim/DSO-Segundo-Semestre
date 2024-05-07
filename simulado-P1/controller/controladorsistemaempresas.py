from models.empresa import Empresa


class ControladorSistemaEmpresas():
    def __init__(self):
        self.__empresas = []

    def inclui_empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            for emp in self.__empresas:
                if empresa.cnpj == emp.cnpj:
                    return None
            self.__empresas.append(empresa)

    def exclui_empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            for emp in self.__empresas:
                if empresa.cnpj == emp.cnpj:
                    self.__empresas.remove(emp)

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        for empresa in self.__empresas:
            if empresa.cnpj == cnpj:
                return empresa
        return None

    @property
    def empresas(self) -> list:
        return self.__empresas

    def calcula_total_impostos(self) -> float:
        total_impo = 0.0
        for emp in self.__empresas:
            total_impo += emp.total_impostos()
        return total_impo
