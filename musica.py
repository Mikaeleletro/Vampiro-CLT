import pyxel

# Definindo os estados do jogo
ESTADO_MENU = 0
ESTADO_JOGANDO = 1
ESTADO_COMO_JOGAR = 2

class Jogo:
    def __init__(self):
        # Inicializa a janela com resolução retrô
        pyxel.init(160, 120, title="Vampiro CLT")
        pyxel.mouse(True)  # Mostra o mouse na tela
        
        self.estado = ESTADO_MENU
        self.musica_tocando = False # Variável para controlar se a música já está tocando
        
        # Configura as trilhas musicais na memória
        self.configurar_musica()
        
        # Inicia o loop principal do Pyxel
        pyxel.run(self.update, self.draw)

    # --- CONFIGURAÇÃO DA MÚSICA ---
    def configurar_musica(self):
        # --- CANAL 0: Melodia (Solidão e Imperfeição) ---
        melodia = (
            "A2 R C3 R E3 R A3 R "
            "G3 R E3 R D3 R C3 R "
            "F2 R A2 R C3 R F3 R "
            "E3 R C3 R B2 R G2 R "
        )
        pyxel.sound(0).set(
            notes=melodia, tones="S", volumes="4", effects="V", speed=16
        )

        # --- CANAL 1: Baixo (A base profunda e quente) ---
        baixo = (
            "A0 R R R A0 R R R "
            "A0 R R R A0 R R R "
            "F0 R R R F0 R R R "
            "F0 R R R F0 R R R "
        )
        pyxel.sound(1).set(
            notes=baixo, tones="T", volumes="5", effects="F", speed=16
        )

        # --- CANAL 2: Harmonia/Cordas (Textura suave de fundo) ---
        harmonia = (
            "E2 A2 C3 E3 C3 A2 E2 A2 "
            "E2 A2 C3 E3 C3 A2 E2 A2 "
            "C2 F2 A2 C3 A2 F2 C2 F2 "
            "C2 F2 A2 C3 A2 F2 C2 F2 "
        )
        pyxel.sound(2).set(
            notes=harmonia, tones="P", volumes="2", effects="N", speed=16
        )

        # --- CANAL 3: Ruído Ambiente (Nostalgia Lo-fi) ---
        ruido = "C0 R R R " * 8
        pyxel.sound(3).set(
            notes=ruido, tones="N", volumes="1210", effects="F", speed=16
        )

    # --- CONTROLE DA MÚSICA ---
    def iniciar_musica(self):
        if not self.musica_tocando:
            pyxel.play(0, 0, loop=True)
            pyxel.play(1, 1, loop=True)
            pyxel.play(2, 2, loop=True)
            pyxel.play(3, 3, loop=True)
            self.musica_tocando = True

    def parar_musica(self):
        if self.musica_tocando:
            pyxel.stop() # Para todos os canais
            self.musica_tocando = False

    def update(self):
        # Lógica principal baseada no estado
        if self.estado == ESTADO_MENU:
            self.update_menu()
            self.parar_musica() # Garante que a música não toque no menu
            
        elif self.estado == ESTADO_COMO_JOGAR:
            self.update_como_jogar()
            self.parar_musica()
            
        elif self.estado == ESTADO_JOGANDO:
            self.update_jogo()
            self.iniciar_musica() # Toca a música apenas na tela do jogo

    def draw(self):
        pyxel.cls(0)  # Limpa a tela
        
        if self.estado == ESTADO_MENU:
            self.desenhar_menu()
        elif self.estado == ESTADO_COMO_JOGAR:
            self.desenhar_como_jogar()
        elif self.estado == ESTADO_JOGANDO:
            self.desenhar_jogo()

    # --- FUNÇÃO AUXILIAR PARA CRIAR BOTÕES ---
    def desenhar_botao_e_verificar_clique(self, x, y, largura, altura, texto, txt_x, txt_y, cor_normal, cor_hover):
        mouse_no_botao = (x <= pyxel.mouse_x <= x + largura and y <= pyxel.mouse_y <= y + altura)
        cor = cor_hover if mouse_no_botao else cor_normal
        
        pyxel.rect(x, y, largura, altura, cor)
        pyxel.rectb(x, y, largura, altura, 7)
        pyxel.text(txt_x, txt_y, texto, 7)
        
        return mouse_no_botao and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)

    # --- LÓGICA E TELA DO MENU ---
    def update_menu(self):
        pass 

    def desenhar_menu(self):
        pyxel.text(57, 20, "VAMPIRO CLT", 7)

        # Botão: INICIAR PARTIDA
        clicou_iniciar = self.desenhar_botao_e_verificar_clique(40, 40, 81, 15, "INICIAR PARTIDA", 45, 45, 5, 11)
        if clicou_iniciar:
            self.estado = ESTADO_JOGANDO
            
        # Botão: COMO JOGAR
        clicou_como = self.desenhar_botao_e_verificar_clique(40, 60, 81, 15, "COMO JOGAR", 53, 65, 5, 11)
        if clicou_como:
            self.estado = ESTADO_COMO_JOGAR

        # Botão: SAIR
        clicou_sair = self.desenhar_botao_e_verificar_clique(40, 80, 81, 15, "SAIR", 70, 85, 2, 8)
        if clicou_sair:
            pyxel.quit() 

    # --- LÓGICA E TELA DE COMO JOGAR ---
    def update_como_jogar(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_ESCAPE):
            self.estado = ESTADO_MENU

    def desenhar_como_jogar(self):
        pyxel.text(60, 10, "COMO JOGAR", 10)
        pyxel.text(10, 30, "1. SOBREVIVA AO EXPEDIENTE.", 7)
        pyxel.text(10, 40, "2. FULMINE SEUS INIMIGOS.", 7)
        pyxel.text(25, 105, "APERTE ENTER PARA VOLTAR", 13)

    # --- LÓGICA E TELA DO JOGO ---
    def update_jogo(self):
        # Se apertar ESC, volta pro menu (e a música vai parar automaticamente no update)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.estado = ESTADO_MENU

    def desenhar_jogo(self):
        # Aqui ficarão os desenhos do seu jogo
        # Coloquei o fundo de "aquarela borrada" que tínhamos antes
        for _ in range(15):
            x = pyxel.rndi(0, 160)
            y = pyxel.rndi(0, 120)
            c = pyxel.rndi(1, 5)
            pyxel.pset(x, y, c)

        pyxel.text(45, 55, "JOGO RODANDO...", 7)
        pyxel.text(35, 75, "ESC PARA VOLTAR", 13)

# Roda o aplicativo
Jogo()