from controle.AbstractCarta import AbstractCarta
from Personagem import Personagem


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

    def valor_total_carta(self) -> int:
        soma = self.__personagem.energia + self.__personagem.habilidade +\
               self.__personagem.resistencia + self.__personagem.velocidade
        return soma
