from Carta import Carta
from controle.AbstractJogador import AbstractJogador


class Jogador(AbstractJogador):
    def __init__(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def mao(self) -> list:
        return self.__mao

    def baixa_carta_da_mao(self) -> Carta:
        if not self.__mao:
            return None
        carta_baixada = self.__mao.pop()
        return carta_baixada

    def inclui_carta_na_mao(self, carta: Carta):
        self.__mao.append(carta)
        return carta
