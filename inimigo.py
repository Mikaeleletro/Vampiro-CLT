import pyxel


class Inimigo():

    def __init__(self, x, y):

        self.hp = 1
        self.x = x
        self.y = y

    def ataque(self, jogador):

        distancia_x = abs(self.x - jogador.x)
        distancia_y = abs(self.y - jogador.y)

        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** (1 / 2)

        if distancia <= 10:
            jogador.hp -= 1

    def movimento(self, jogador):
        
        velocidade = 1
        direcao_x = jogador.x - self.x
        direcao_y = jogador.y - self.y
        distancia = ((direcao_x ** 2) + (direcao_y ** 2)) ** (1 / 2)
        if distancia != 0:
            direcao_x /= distancia
            direcao_y /= distancia
        self.x += direcao_x * velocidade
        self.y += direcao_y * velocidade
            

    def desenhar(self):

        pyxel.blt(self.x,self.y,0,32,0,16,16,0)