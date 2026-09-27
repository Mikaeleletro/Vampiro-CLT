import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil


TILE_CHAO = (0, 6)

projetis = []
cooldown_tiro = 0
camera_x = 0

jogador = Personagem()

inimigos = [
    Inimigo(50, 147, 2),
    Inimigo(100, 140, 1)
]


def update():

    global cooldown_tiro
    global camera_x

    jogador.movimento()
    jogador.pulo()
    jogador.gravidade()
    jogador.colisao()

    camera_x = jogador.x - 80

    if camera_x < 0:
        camera_x = 0

    if cooldown_tiro > 0:
        cooldown_tiro -= 1

    for inimigo in inimigos:

        inimigo.movimento(jogador)
        inimigo.ataque(jogador)
        inimigo.colisao(jogador)

    for i in range(len(inimigos)):

        for j in range(i + 1, len(inimigos)):

            inimigos[i].colisao_inimigo(inimigos[j])

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and cooldown_tiro == 0:

        novo_projetil = Projetil(
            jogador.x,
            jogador.y,
            jogador.direcao
        )

        projetis.append(novo_projetil)

        cooldown_tiro = 20

    for projetil in projetis[:]:

        projetil.movimento()

        for inimigo in inimigos:

            inimigo_esquerda = inimigo.x - 10
            inimigo_direita = inimigo.x + 6

            inimigo_cima = inimigo.y - 10
            inimigo_baixo = inimigo.y + 6

            projetil_esquerda = projetil.x
            projetil_direita = projetil.x + 5

            projetil_cima = projetil.y
            projetil_baixo = projetil.y + 5

            if (
                projetil_direita > inimigo_esquerda
                and projetil_esquerda < inimigo_direita
                and projetil_baixo > inimigo_cima
                and projetil_cima < inimigo_baixo
            ):

                inimigo.hp -= projetil.dano

                projetis.remove(projetil)

                break

    for inimigo in inimigos[:]:

        if inimigo.hp <= 0:
            inimigos.remove(inimigo)


def draw():

    pyxel.cls(0)

    pyxel.bltm(
        -camera_x,
        153,
        0,
        0,
        0,
        150,
        20
    )

    if jogador.hp > 0:

        jogador.desenhar(camera_x)

        for inimigo in inimigos:
            inimigo.desenhar(camera_x)

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
        projetil.desenhar(camera_x)


pyxel.init(161, 161)

pyxel.load("my_resource.pyxres")

pyxel.run(update, draw)