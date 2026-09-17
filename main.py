import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil


TILE_CHAO = (0, 6)

projetis = []
cooldown_tiro = 0

jogador = Personagem()

inimigos = [
    Inimigo(50, 50),
]


def update():

    global cooldown_tiro

    jogador.movimento()
    jogador.pulo()
    jogador.gravidade()
    jogador.colisao()


    if cooldown_tiro > 0:
        cooldown_tiro -= 1


    # INIMIGOS
    for inimigo in inimigos:

        inimigo.movimento(jogador)
        for outro in inimigos:

            if inimigo != outro:
                inimigo.colisao_inimigo(outro)

        inimigo.ataque(jogador)
        inimigo.colisao(jogador)


    # TIRO
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and cooldown_tiro == 0:

        novo_projetil = Projetil(
            jogador.x,
            jogador.y,
            jogador.direcao
        )

        projetis.append(novo_projetil)

        cooldown_tiro = 20


    # PROJÉTEIS
    for projetil in projetis:
        projetil.movimento()


def draw():

    pyxel.cls(0)

    # TILEMAP
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


        # INIMIGOS
        for inimigo in inimigos:
            inimigo.desenhar()


        # VIDA
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


    # PROJÉTEIS
    for projetil in projetis:
        projetil.desenhar()


pyxel.init(161, 161)

pyxel.load("my_resource.pyxres")

pyxel.run(update, draw)