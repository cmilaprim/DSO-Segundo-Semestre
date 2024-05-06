from AbstractControladorJogo import AbstractControladorJogo
from entidade.Mesa import Mesa
from controle.AbstractPersonagem import Tipo
from entidade.Personagem import Personagem
from entidade.Carta import Carta
from entidade.Jogador import Jogador


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia,
                                habilidade,
                                velocidade,
                                resistencia,
                                tipo)
        self.__personagems.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        nova_carta = Carta(personagem)
        self.__baralho.append(nova_carta)
        return nova_carta

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            carta_jogador1 = mesa.carta_jogador1
            carta_jogador2 = mesa.carta_jogador2
            valor_carta_jogador1 = carta_jogador1.valor_total_carta()
            valor_carta_jogador2 = carta_jogador2.valor_total_carta()

            if valor_carta_jogador1 > valor_carta_jogador2:
                mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
                mesa.jogador1.inclui_carta_na_mao(carta_jogador2)
                if len(mesa.jogador2.mao) == 0:
                    return mesa.jogador1
                else:
                    return None
            elif valor_carta_jogador2 > valor_carta_jogador1:
                mesa.jogador2.inclui_carta_na_mao(carta_jogador1)
                mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
                if len(mesa.jogador1.mao) == 0:
                    return mesa.jogador2
                else:
                    return None
            else:
                mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
                mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
                if len(mesa.jogador1.mao) == 0 or len(mesa.jogador2.mao) == 0:
                    return None
