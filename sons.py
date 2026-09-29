import pyxel


SOM_TIRO = 2
SOM_INIMIGO_DERROTADO = 3
SOM_LEVEL_UP = 4
SOM_GAME_OVER = 5
SOM_VITORIA = 6


def configurar_sons():

    pyxel.sounds[SOM_TIRO].set("c3", "p", "7", "f", 5)
    pyxel.sounds[SOM_INIMIGO_DERROTADO].set(
        "c3e3g3", "t", "765", "f", 5
    )
    pyxel.sounds[SOM_LEVEL_UP].set(
        "c3e3g3c4", "t", "6777", "n", 6
    )
    pyxel.sounds[SOM_GAME_OVER].set(
        "g2e2c2", "s", "765", "f", 12
    )
    pyxel.sounds[SOM_VITORIA].set(
        "c3e3g3c4", "p", "6777", "n", 8
    )


def tocar_som(som):

    pyxel.play(3, som)
