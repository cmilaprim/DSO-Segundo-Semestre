from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):

    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def chamados(self):
        return self.__chamados

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        total_chamados_por_tipo = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo and chamado.tipo.codigo == tipo.codigo:
                total_chamados_por_tipo += 1
        return total_chamados_por_tipo

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico,
                       titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:
        novo_chamado = Chamado(data, cliente,
                               tecnico, titulo, descricao, prioridade, tipo)
        if isinstance(data, Date) and isinstance(cliente, Cliente) and\
            isinstance(tecnico, Tecnico) and isinstance(titulo, str) and\
            isinstance(descricao, str) and isinstance(prioridade, int) and\
                isinstance(tipo, TipoChamado):
            for chamado in self.__chamados:
                if (chamado.data == novo_chamado.data
                    and chamado.cliente == novo_chamado.cliente
                    and chamado.tecnico == novo_chamado.tecnico
                        and chamado.tipo == novo_chamado.tipo):
                    return None
            self.__chamados.append(novo_chamado)
            return novo_chamado

    def inclui_tipochamado(self, codigo: int,
                           nome: str,
                           descricao: str) -> TipoChamado:
        novo_tipoChamado = TipoChamado(codigo, descricao, nome)
        for tipoChamado in self.__tipos_chamados:
            if (tipoChamado.codigo == novo_tipoChamado.codigo or
                tipoChamado.nome == novo_tipoChamado.nome or
                    tipoChamado.descricao == novo_tipoChamado.descricao):
                return None
        self.__tipos_chamados.append(novo_tipoChamado)
        return novo_tipoChamado
