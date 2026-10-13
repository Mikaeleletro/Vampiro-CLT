import pyxel


class Mapa:

    def __init__(self):
        self.tilemap_jogo = 0              # Tilemap 0: Chão e plataformas
        self.tilemap_fundo_proximo = 1     # Tilemap 1: árvores (movem-se a 30%)
        self.tilemap_fundo_distante = 2    # Tilemap 2: prédios(movem-se a 10%)

    # --- 1. DESENHAR O MAPA DE FUNDO MAIS DISTANTE (prédios) ---
    def desenhar_fundo_paralaxe_2(self, camera_x):
        # Limpa o ecrã com a cor do céu ANTES de tudo
        pyxel.cls(1)
        
        # Move a 10% da velocidade da câmara
        pos_x_fundo = -(camera_x * 0.1)

        pyxel.bltm(
            x=pos_x_fundo,
            y=32,
            tm=self.tilemap_fundo_distante,
            u=0,
            v=0,
            w=1000,
            h=161,
            colkey=0
        )

    # --- 2. DESENHAR O MAPA DE FUNDO MAIS PRÓXIMO (árvores) ---
    def desenhar_fundo_paralaxe_1(self, camera_x):
        # Move a 30% da velocidade da câmara
        pos_x_fundo = -(camera_x * 0.3)

        pyxel.bltm(
            x=pos_x_fundo,
            y=32,
            tm=self.tilemap_fundo_proximo,
            u=0,
            v=0,
            w=1000,
            h=161,
            colkey=0
        )

    # --- 3. DESENHAR O MAPA NORMAL (INTERATIVO) ---
    def desenhar_mapa_principal(self, camera_x):
        # Desenha o Tilemap 0 acompanhando a câmara a 100% da velocidade
        pyxel.bltm(
            x=-camera_x,
            y=32,
            tm=self.tilemap_jogo,
            u=0,
            v=0,
            w=1000,
            h=161,
            colkey=0
        )

    
    