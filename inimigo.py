import pyxel


class Inimigo():

    def __init__(self, x, y):

        self.hp = 1
        self.x = x
        self.y = y

        self.walk = 32
        self.contador_walk = 0
        self.direcao = "direita"

    def ataque(self, jogador):

        distancia_x = abs(self.x - jogador.x)
        distancia_y = abs(self.y - jogador.y)

        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5

        if distancia <= 10:
            jogador.hp -= 1

    def movimento(self, jogador):

        velocidade = 1

        direcao_x = jogador.x - self.x
        direcao_y = jogador.y - self.y

        distancia = ((direcao_x ** 2) + (direcao_y ** 2)) ** 0.5

        if distancia != 0:
            direcao_x /= distancia
            direcao_y /= distancia

        self.x += direcao_x * velocidade
        self.y += direcao_y * velocidade

        if jogador.x > self.x:
            self.direcao = "direita"

        elif jogador.x < self.x:
            self.direcao = "esquerda"

        self.animacao()

    def colisao(self, jogador):

        distancia_x = jogador.x - self.x
        distancia_y = jogador.y - self.y

        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5

        if distancia < 16:

            if distancia != 0:

                distancia_x /= distancia
                distancia_y /= distancia

                self.x = jogador.x - distancia_x * 1
                self.y = jogador.y - distancia_y * 1

    def animacao(self):

        self.contador_walk += 1

        if self.contador_walk >= 5:

            self.contador_walk = 0

            if self.walk == 32:
                self.walk = 48

            elif self.walk == 48:
                self.walk = 32

    def desenhar(self):

        if self.direcao == "direita":

            pyxel.blt(
                self.x - 10,
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
                self.x - 10,
                self.y - 10,
                0,
                self.walk,
                0,
                -16,
                16,
                0
            )
    def colisao_inimigo(self, outro):

        distancia_x = outro.x - self.x
        distancia_y = outro.y - self.y

        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5

        if distancia < 16:

            if distancia != 0:

                distancia_x /= distancia
                distancia_y /= distancia

                self.x -= distancia_x * 16
                self.y -= distancia_y * 16
