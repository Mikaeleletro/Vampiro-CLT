#survival vampire
import pyxel

class Coracao():

    def __init__(self):

        self.hp = 50

    def desenhar(self):

        pyxel.rect(80,80,4,4,7)

class Inimigo():

    def __init__(self,x,y):
        self.hp = 1
        self.y = y
        self.x = x
        
    def movimento(self):
        
        distancia_x = abs(self.x - 80)
        distancia_y = abs(self.y - 80)
        distancia = ((distancia_x)**2+(distancia_y)**2)**(1/2)
        
        if distancia >= 9:
            
            if coracao.hp != 0:
                
                if self.x > 80:
                    self.x -= 1
                if self.x < 80:
                    self.x += 1
                if self.y > 80:
                    self.y -= 1
                if self.y < 80:
                    self.y += 1
                    
        if distancia <= 10:
            coracao.hp -= 1
            
        if coracao.hp <= 0:
            coracao.hp = 0
            
        if coracao.hp == 0: 
              
            if jogador.x < self.x:
                self.x -= 1
            if jogador.x > self.x:
                self.x += 1
            if jogador.y < self.y:
                self.y -= 1
            if jogador.y > self.y:
                self.y += 1

    def desenhar(self):
        pyxel.pset(self.x,self.y,7)


class Personagem():
    def __init__(self):
        
        self.x = 80
        self.y = 60
        self.direcao = "esquerda"
        
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

        x = pyxel.mouse_x
        y = pyxel.mouse_y
        
        pyxel.rect(self.x,self.y,2,2,7)
        if pyxel.btn(pyxel.KEY_SPACE):
            pyxel.line(self.x,self.y,x,y,7)
        
        if self.direcao == "cima":
            pyxel.rect(self.x,self.y-2,2,2,8)
            
        if self.direcao == "baixo":
            pyxel.rect(self.x,self.y+2,2,2,8)
            
        if self.direcao == "direita":
            pyxel.rect(self.x+2,self.y,2,2,8)
            
        if self.direcao == "esquerda":
            pyxel.rect(self.x-2,self.y,2,2,8)
            
    def colicao(self):
        
        if self.x <= 0:
            self.x = 0
            
        if self.x >= 159:
            self.x = 159
            
        if self.y >= 159:
            self.y = 159
            
        if self.y <= 0:
            self.y = 0
    
jogador = Personagem()
inimigo = Inimigo(5,5)
coracao = Coracao()

def update():
    
    jogador.movimento()
    jogador.colicao()
    inimigo.movimento()

def draw():
    
    pyxel.cls(0)
    jogador.desenhar()
    inimigo.desenhar()
    coracao.desenhar()
    pyxel.rect(2,2,49*(coracao.hp/50),9,8)
    pyxel.rectb(1,1,50,10,7)
    
pyxel.init(161,161)
pyxel.run(update,draw)
        
