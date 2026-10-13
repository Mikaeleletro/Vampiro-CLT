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

    def desenhar(self, camera_x):

        tamanho = 5

        pyxel.line(
            self.x - camera_x,
            self.y+10,
            self.x - camera_x + self.direcao_x * tamanho,
            self.y+10,
            7
        )


class AtaqueEspecial:

    def __init__(self, jogador, dano, frames_u, v):

        self.jogador = jogador # O ataque conhece o jogador para se colar a ele
        self.dano = dano
        
        # Variáveis de Animação
        self.frames_u = frames_u 
        self.v = v
        self.frame_atual = 0
        self.contador_animacao = 0
        
        # Tempo de vida do golpe (10 frames = um terço de segundo)
        self.tempo_vida = 10 
        
        self.atualizar_posicao()

    def atualizar_posicao(self):
        # Cola o ataque na frente do jogador dependendo de onde ele olha
        if self.jogador.direcao == "direita":
            self.x = self.jogador.x + 8
            self.largura = 16
        elif self.jogador.direcao == "esquerda":
            self.x = self.jogador.x - 16
            self.largura = -16
            
        self.y = self.jogador.y

    def movimento(self):
        # Atualiza a posição a cada frame e reduz a vida do golpe
        self.atualizar_posicao()
        self.animacao()
        self.tempo_vida -= 1 

    def animacao(self):
        self.contador_animacao += 1
        
        if self.contador_animacao >= 5: 
            self.contador_animacao = 0
            self.frame_atual += 1
        
            if self.frame_atual >= len(self.frames_u):
                self.frame_atual = len(self.frames_u) - 1

    def desenhar(self, camera_x):
        pyxel.blt(
            self.x - camera_x,
            self.y, 
            0,
            self.frames_u[self.frame_atual], 
            self.v, 
            self.largura, 
            16,
            0
        )