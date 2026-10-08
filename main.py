import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil
from efeitos import (
    criar_efeito,
    atualizar_efeitos,
    desenhar_efeitos
)
import sons
from telas import (
    clicou_iniciar,
    desenhar_menu,
    desenhar_hud,
    desenhar_game_over,
    desenhar_vitoria
)


TILE_CHAO = (0, 6)

MENU = "menu"
JOGANDO = "jogando"
GAME_OVER = "game_over"
VITORIA = "vitoria"

projetis = []
efeitos = []
cooldown_tiro = 0
camera_x = 0

inimigos_derrotados = 0
tempo_inicio = 0
tempo_partida = 0
estado_jogo = MENU

jogador = Personagem()

inimigos = [
    Inimigo(50, 147, 2),
    Inimigo(100, 140, 1)
]


def iniciar_partida():

    global jogador
    global inimigos
    global projetis
    global efeitos
    global cooldown_tiro
    global camera_x
    global inimigos_derrotados
    global tempo_inicio
    global tempo_partida
    global estado_jogo

    jogador = Personagem()

    inimigos = [
        Inimigo(50, 147, 2),
        Inimigo(100, 140, 1)
    ]

    projetis = []
    efeitos = []
    cooldown_tiro = 0
    camera_x = 0

    inimigos_derrotados = 0
    tempo_inicio = pyxel.frame_count
    tempo_partida = 0
    estado_jogo = JOGANDO


def update():

    global cooldown_tiro
    global camera_x
    global inimigos_derrotados
    global tempo_partida
    global estado_jogo

    if estado_jogo == MENU:

        if clicou_iniciar():
            iniciar_partida()

        return

    if estado_jogo == GAME_OVER or estado_jogo == VITORIA:

        if pyxel.btnp(pyxel.KEY_RETURN):
            iniciar_partida()

        return

    tempo_partida = (pyxel.frame_count - tempo_inicio) // 30

    atualizar_efeitos(efeitos)

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

    if jogador.hp <= 0:
        jogador.hp = 0
        estado_jogo = GAME_OVER
        sons.tocar_som(sons.SOM_GAME_OVER)
        return

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

        criar_efeito(efeitos, jogador.x, jogador.y + 10, 10, 3)
        sons.tocar_som(sons.SOM_TIRO)

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

                criar_efeito(efeitos, inimigo.x, inimigo.y, 7, 3)

                break

    for inimigo in inimigos[:]:

        if inimigo.hp <= 0:

            inimigos.remove(inimigo)
            inimigos_derrotados += 1

            subiu_nivel = jogador.ganhar_xp(10)

            criar_efeito(efeitos, inimigo.x, inimigo.y, 8, 8)

            if subiu_nivel:
                criar_efeito(efeitos, jogador.x, jogador.y, 11, 15)
                sons.tocar_som(sons.SOM_LEVEL_UP)

            else:
                sons.tocar_som(sons.SOM_INIMIGO_DERROTADO)

    if len(inimigos) == 0:
        estado_jogo = VITORIA
        sons.tocar_som(sons.SOM_VITORIA)


def draw():

    if estado_jogo == MENU:
        desenhar_menu()
        return

    pyxel.cls(0)

    pyxel.bltm(
        -camera_x,
        153,
        0,
        0,
        0,
        1000,
        20
    )

    if jogador.hp > 0:
        jogador.desenhar(camera_x)

    for inimigo in inimigos:
        inimigo.desenhar(camera_x)

    for projetil in projetis:
        projetil.desenhar(camera_x)

    desenhar_efeitos(efeitos, camera_x)

    desenhar_hud(
        jogador,
        tempo_partida,
        inimigos_derrotados
    )

    if estado_jogo == GAME_OVER:
        desenhar_game_over()

    elif estado_jogo == VITORIA:
        desenhar_vitoria()


pyxel.init(161, 161)

pyxel.load("my_resource.pyxres")

sons.configurar_sons()

pyxel.mouse(True)

pyxel.run(update, draw)
