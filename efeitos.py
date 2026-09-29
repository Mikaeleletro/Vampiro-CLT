import pyxel


class Particula():

    def __init__(self, x, y, cor):

        self.x = x
        self.y = y
        self.cor = cor

        self.vx = pyxel.rndi(-2, 2)
        self.vy = pyxel.rndi(-2, 1)
        self.tempo = 15


    def movimento(self):

        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1
        self.tempo -= 1


    def desenhar(self, camera_x):

        pyxel.pset(
            self.x - camera_x,
            self.y,
            self.cor
        )


def criar_efeito(efeitos, x, y, cor, quantidade):

    for i in range(quantidade):
        efeitos.append(Particula(x, y, cor))


def atualizar_efeitos(efeitos):

    for particula in efeitos[:]:

        particula.movimento()

        if particula.tempo <= 0:
            efeitos.remove(particula)


def desenhar_efeitos(efeitos, camera_x):

    for particula in efeitos:
        particula.desenhar(camera_x)
