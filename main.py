import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil
projetis = []
jogador = Personagem()

inimigo = Inimigo(5, 5)
inimigo1 = Inimigo(100, 100)


def update():
    
    jogador.movimento()
    jogador.colisao()

    inimigo.movimento(jogador)
    inimigo1.movimento(jogador)

    inimigo.ataque(jogador)
    inimigo1.ataque(jogador)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):

        projetil = Projetil(
            jogador.x,
            jogador.y,
            pyxel.mouse_x,
            pyxel.mouse_y
        )
        projetis.append(projetil)
    for projetil in projetis:
        projetil.movimento()

def draw():

    pyxel.cls(0)
    pyxel.pset(jogador.x,jogador.y,7)
    if jogador.hp > 0:

        inimigo1.desenhar()
        inimigo.desenhar()
        jogador.desenhar()

        # Barra do jogador
        pyxel.rect(2, 11, 49 * (jogador.hp / 1000), 9, 8)
        pyxel.rectb(1, 10, 50, 10, 7)

    else:

        pyxel.text(50, 50, "Voce Perdeu!", 7)
    for projetil in projetis:
        projetil.desenhar()

pyxel.init(161, 161)

pyxel.load("my_resource.pyxres")

pyxel.run(update, draw)