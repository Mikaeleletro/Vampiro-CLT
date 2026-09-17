import pyxel


class Personagem():

    def __init__(self):

        self.x = 4
        self.y = 135

        self.direcao = "esquerda"
        self.hp = 1000

        self.walk = 0
        self.contador_walk = 0

        self.vy = 0
        self.aceleracao = 0.8
        self.forca_pulo = -8

        self.no_chao = False


    def movimento(self):

        andando = False

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direcao = "esquerda"
            andando = True

        elif pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direcao = "direita"
            andando = True

        if andando:
            self.animacao()

        else:
            self.walk = 0
            self.contador_walk = 0


    def animacao(self):

        self.contador_walk += 1

        if self.contador_walk >= 5:

            self.contador_walk = 0

            if self.walk == 0:
                self.walk = 16

            elif self.walk == 16:
                self.walk = 0


    def desenhar(self):

        if self.direcao == "direita":
            pyxel.blt(
                self.x - 8,
                self.y + 1,
                0,
                self.walk,
                0,
                16,
                16,
                0
            )

        if self.direcao == "esquerda":
            pyxel.blt(
                self.x - 8,
                self.y + 1,
                0,
                self.walk,
                0,
                -16,
                16,
                0
            )


    def colisao(self,):

        if self.x <= 0:
            self.x = 0

        if self.x >= 159:
            self.x = 159

        if self.y >= 136:
            self.y = 136
            self.vy = 0

        if self.y <= 0:
            self.y = 0
            self.vy = 0


    def gravidade(self):

        self.vy += self.aceleracao
        self.y += self.vy


    def pulo(self):

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = self.forca_pulo