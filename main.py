import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil


TILE_CHAO = 1

projetis = []
cooldown_tiro = 0

jogador = Personagem()

inimigo = Inimigo(50, 50)
inimigo1 = Inimigo(100, 100)


def tem_chao(x, y):

    tile_x = x // 8
    tile_y = (y - 153) // 8

    tile = pyxel.tilemaps[0].pget(tile_x, tile_y)

    return tile == (0, 6)


def update():

    global cooldown_tiro

    jogador.movimento()
    jogador.pulo()
    jogador.gravidade()
    jogador.colisao(tem_chao)


    if cooldown_tiro > 0:
        cooldown_tiro -= 1


    inimigo.movimento(jogador)
    inimigo1.movimento(jogador)

    inimigo.ataque(jogador)
    inimigo.colisao(jogador)

    inimigo1.ataque(jogador)
    inimigo1.colisao(jogador)


    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and cooldown_tiro == 0:

        novo_projetil = Projetil(
            jogador.x,
            jogador.y,
            jogador.direcao
        )

        projetis.append(novo_projetil)

        cooldown_tiro = 20


    for projetil in projetis:
        projetil.movimento()

def draw():

    pyxel.cls(0)

    # Tilemap
    pyxel.bltm(
    0,
    153,
    0,
    0,
    0,
    150,
    20
)


    if jogador.hp > 0:

        jogador.desenhar()
        inimigo.desenhar()

        pyxel.rect(
            2,
            11,
            49 * (jogador.hp / 1000),
            9,
            8
        )

        pyxel.rectb(
            1,
            10,
            50,
            10,
            7
        )

    else:

        pyxel.text(
            50,
            50,
            "Voce Perdeu!",
            7
        )


    for projetil in projetis:
        projetil.desenhar()


pyxel.init(161, 161)

pyxel.load("my_resource.pyxres")

pyxel.run(update, draw)