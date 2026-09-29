import pyxel


def clicou_iniciar():

    mouse_no_botao = (
        40 <= pyxel.mouse_x <= 120
        and 75 <= pyxel.mouse_y <= 95
    )

    return (
        pyxel.btnp(pyxel.KEY_RETURN)
        or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and mouse_no_botao
    )


def desenhar_menu():

    pyxel.cls(0)
    pyxel.text(57, 42, "VAMPIRO CLT", 7)
    pyxel.text(33, 58, "DERROTE TODOS OS INIMIGOS", 6)

    mouse_no_botao = (
        40 <= pyxel.mouse_x <= 120
        and 75 <= pyxel.mouse_y <= 95
    )

    cor_botao = 11 if mouse_no_botao else 5

    pyxel.rect(40, 75, 81, 21, cor_botao)
    pyxel.rectb(40, 75, 81, 21, 7)
    pyxel.text(50, 82, "INICIAR PARTIDA", 7)
    pyxel.text(43, 110, "CLIQUE OU APERTE ENTER", 13)


def desenhar_hud(jogador, tempo, derrotados):

    pyxel.rect(0, 0, 161, 32, 0)
    pyxel.text(2, 2, "VIDA: " + str(jogador.hp), 7)

    pyxel.rect(2, 11, 49 * (jogador.hp / 1000), 9, 8)
    pyxel.rectb(1, 10, 50, 10, 7)

    pyxel.text(58, 2, "NIVEL: " + str(jogador.nivel), 7)
    pyxel.text(
        58,
        12,
        "XP: " + str(jogador.xp) + "/" + str(jogador.xp_proximo_nivel),
        7
    )

    pyxel.text(2, 24, "TEMPO: " + str(tempo) + "s", 7)
    pyxel.text(70, 24, "INIMIGOS: " + str(derrotados), 7)


def desenhar_game_over():

    pyxel.rect(25, 55, 111, 51, 0)
    pyxel.rectb(25, 55, 111, 51, 8)
    pyxel.text(55, 66, "VOCE PERDEU!", 8)
    pyxel.text(37, 84, "ENTER PARA TENTAR NOVAMENTE", 7)


def desenhar_vitoria():

    pyxel.rect(25, 55, 111, 51, 0)
    pyxel.rectb(25, 55, 111, 51, 11)
    pyxel.text(53, 66, "VOCE VENCEU!", 11)
    pyxel.text(37, 84, "ENTER PARA JOGAR NOVAMENTE", 7)
