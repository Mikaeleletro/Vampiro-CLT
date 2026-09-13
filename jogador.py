import pyxel


class Personagem():

    def __init__(self):
        self.x = 80
        self.y = 60
        self.direcao = "esquerda"
        self.hp = 1000

    def movimento(self):

        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
            self.direcao = "cima"

        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
            self.direcao = "baixo"

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direcao = "esquerda"

        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direcao = "direita"

    def desenhar(self):

        pyxel.blt(
            self.x,
            self.y,
            0,
            0,
            0,
            16,
            16,
            0
        )

    def colisao(self):

        if self.x <= 0:
            self.x = 0

        if self.x >= 159:
            self.x = 159

        if self.y >= 159:
            self.y = 159

        if self.y <= 0:
            self.y = 0