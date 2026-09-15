import pyxel


class Personagem():

    def __init__(self):
        self.x = 80
        self.y = 60
        self.direcao = "esquerda"
        self.hp = 1000
        self.walk = 0
        self.contador_walk = 0
    def movimento(self):

        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
            self.direcao = "cima"
            
        elif pyxel.btn(pyxel.KEY_S):
            self.y += 2
            self.direcao = "baixo"

        elif pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direcao = "esquerda"
            
        elif pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direcao = "direita"
            
    def desenhar(self):

        if self.direcao == "direita":
            pyxel.blt(-5+self.x,self.y,0,self.walk,0,16,16,0)

        if self.direcao == "esquerda":
            pyxel.blt(self.x,self.y,0,0,self.walk,-16,16,0)

        if self.direcao == "baixo":
            pyxel.blt(self.x,self.y,0,self.walk,16,16,16,0)

        if self.direcao == "cima":
            pyxel.blt(self.x,self.y,0,self.walk,32,16,16,0)
            
    def animacao(self):
        self.contador_walk += 1
        
        
          
    def colisao(self):

        if self.x <= 0:
            self.x = 0

        if self.x >= 159:
            self.x = 159

        if self.y >= 159:
            self.y = 159

        if self.y <= 0:
            self.y = 0