import pyxel


class Projetil():

    def __init__(self, x, y, direcao):

        self.x = x
        self.y = y

        self.velocidade = 3
        self.dano = 1

        if direcao == "direita":
            self.direcao_x = 1

        elif direcao == "esquerda":
            self.direcao_x = -1

        self.direcao_y = 0

    def movimento(self):

        self.x += self.direcao_x * self.velocidade
        self.y += self.direcao_y * self.velocidade

    def desenhar(self):
        tamanho = 5
        pyxel.line(
            self.x,
            self.y+10,
            self.x + self.direcao_x * tamanho,
            self.y+10,
            7
        )