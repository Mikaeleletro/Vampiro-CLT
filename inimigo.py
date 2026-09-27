import pyxel


class Inimigo():

    def __init__(self, x, y, tipo):

        self.hp = 2
        self.x = x
        self.y = y
        self.tipo = tipo

        self.walk = 32
        self.contador_walk = 0
        self.direcao = "direita"


    def ataque(self, jogador):

        inimigo_esquerda = self.x - 10
        inimigo_direita = self.x + 6

        inimigo_cima = self.y - 10
        inimigo_baixo = self.y + 6

        jogador_esquerda = jogador.x - 8
        jogador_direita = jogador.x + 8

        jogador_cima = jogador.y
        jogador_baixo = jogador.y + 16

        if (
            inimigo_direita > jogador_esquerda
            and inimigo_esquerda < jogador_direita
            and inimigo_baixo > jogador_cima
            and inimigo_cima < jogador_baixo
        ):

            jogador.hp -= 1


    def movimento(self, jogador):

        velocidade = 1

        if jogador.x > self.x:

            self.x += velocidade
            self.direcao = "direita"

        elif jogador.x < self.x:

            self.x -= velocidade
            self.direcao = "esquerda"

        self.animacao()


    def colisao(self, jogador):

        inimigo_esquerda = self.x - 10
        inimigo_direita = self.x + 6

        inimigo_cima = self.y - 10
        inimigo_baixo = self.y + 6

        jogador_esquerda = jogador.x - 8
        jogador_direita = jogador.x + 8

        jogador_cima = jogador.y
        jogador_baixo = jogador.y + 16

        if (
            inimigo_direita > jogador_esquerda
            and inimigo_esquerda < jogador_direita
            and inimigo_baixo > jogador_cima
            and inimigo_cima < jogador_baixo
        ):

            if self.x < jogador.x:

                self.x = jogador.x - 18

            else:

                self.x = jogador.x + 18


    def colisao_inimigo(self, outro):

        distancia_x = outro.x - self.x
        distancia = abs(distancia_x)

        if distancia < 16:

            if distancia_x > 0:

                self.x -= 1
                outro.x += 1

            elif distancia_x < 0:

                self.x += 1
                outro.x -= 1


    def animacao(self):

        self.contador_walk += 1

        if self.contador_walk >= 5:

            self.contador_walk = 0

            if self.walk == 32:

                self.walk = 48

            elif self.walk == 48:

                self.walk = 32


    def desenhar(self, camera_x):

        if self.tipo == 1:

            if self.direcao == "direita":

                pyxel.blt(
                    self.x - camera_x - 10,
                    self.y - 10,
                    0,
                    self.walk,
                    0,
                    16,
                    16,
                    0
                )

            elif self.direcao == "esquerda":

                pyxel.blt(
                    self.x - camera_x - 10,
                    self.y - 10,
                    0,
                    self.walk,
                    0,
                    -16,
                    16,
                    0
                )

        elif self.tipo == 2:

            if self.direcao == "direita":

                pyxel.blt(
                    self.x - camera_x - 10,
                    self.y - 10,
                    0,
                    self.walk - 32,
                    16,
                    16,
                    16,
                    0
                )

            elif self.direcao == "esquerda":

                pyxel.blt(
                    self.x - camera_x - 10,
                    self.y - 10,
                    0,
                    self.walk - 32,
                    16,
                    -16,
                    16,
                    0
                )