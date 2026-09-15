import pyxel


class Projetil():

    def __init__(self, x, y, alvo_x, alvo_y):

        self.x = x
        self.y = y

        self.alvo_x = alvo_x
        self.alvo_y = alvo_y

        self.velocidade = 3
        self.dano = 1
        direcao_x = alvo_x - x
        direcao_y = alvo_y - y

        distancia = ((direcao_x ** 2) + (direcao_y ** 2)) ** 0.5

        if distancia != 0:
            direcao_x /= distancia
            direcao_y /= distancia

        self.direcao_x = direcao_x
        self.direcao_y = direcao_y

    def movimento(self):

        self.x += self.direcao_x * self.velocidade
        self.y += self.direcao_y * self.velocidade

    def desenhar(self):

        pyxel.rect(
            self.x,
            self.y,
            2,
            2,
            11
        )

        tamanho = 5

        pyxel.line(
            self.x,
            self.y,
            self.x + self.direcao_x * tamanho,
            self.y + self.direcao_y * tamanho,
            7
        )
