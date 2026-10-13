import pyxel

from jogador import Personagem
from inimigo import Inimigo
from projetil import Projetil, AtaqueEspecial
from mapa import Mapa

from efeitos import (
    criar_efeito,
    atualizar_efeitos,
    desenhar_efeitos
)
import sons
from telas import (
    clicou_iniciar,
    desenhar_menu,
    desenhar_hud,
    desenhar_game_over,
    desenhar_vitoria
)

MENU = "menu"
JOGANDO = "jogando"
GAME_OVER = "game_over"
VITORIA = "vitoria"
UPGRADE = "upgrade"
contador_kills_upgrade = 0

projetis = []
ataques_especiais = []
efeitos = []
cooldown_tiro = 0
camera_x = 0

inimigos_derrotados = 0
tempo_inicio = 0
tempo_partida = 0
estado_jogo = MENU

mapa = Mapa()


def iniciar_partida():

    global jogador
    global inimigos
    global projetis
    global ataques_especiais
    global efeitos
    global cooldown_tiro
    global camera_x
    global inimigos_derrotados
    global tempo_inicio
    global tempo_partida
    global estado_jogo
    global contador_kills_upgrade
    
    jogador = Personagem()
    inimigos = [
        Inimigo(50, 145, 2),
        Inimigo(100, 140, 1),
        Inimigo(200,139,3),
        Inimigo(235,139,3),
        Inimigo(250,139,3)
    ]

    projetis = []
    ataques_especiais = []
    efeitos = []
    cooldown_tiro = 0
    camera_x = 0

    inimigos_derrotados = 0
    contador_kills_upgrade = 0
    tempo_inicio = pyxel.frame_count
    tempo_partida = 0
    estado_jogo = JOGANDO


def update():
    global contador_kills_upgrade
    global cooldown_tiro
    global camera_x
    global inimigos_derrotados
    global tempo_partida
    global estado_jogo

    if estado_jogo == MENU:
        if clicou_iniciar():
            iniciar_partida()
        return

    if estado_jogo == GAME_OVER or estado_jogo == VITORIA:
        if pyxel.btnp(pyxel.KEY_RETURN):
            iniciar_partida()
        return
    
    if estado_jogo == UPGRADE:
        if pyxel.btnp(pyxel.KEY_1):
            jogador.tipo_ataque_especial = 1
            estado_jogo = JOGANDO
            
        elif pyxel.btnp(pyxel.KEY_2):
            # NOVO: Reduz o cooldown do tiro normal (limite mínimo de 5 frames)
            if jogador.limite_cooldown_tiro > 5:
                jogador.limite_cooldown_tiro -= 5
            estado_jogo = JOGANDO
            
        return 
            
    tempo_partida = (pyxel.frame_count - tempo_inicio) // 30

    # Lógica Automática do Ataque Especial
    if jogador.tipo_ataque_especial == 1:
        if jogador.cooldown_especial > 0:
            jogador.cooldown_especial -= 1
        else:
            novo_ataque = AtaqueEspecial(jogador, 3, [0, 16], 32)
            jogador.cooldown_especial = 150 # 5 segundos
            ataques_especiais.append(novo_ataque)
            sons.tocar_som(sons.SOM_TIRO)

    atualizar_efeitos(efeitos)

    # 1. Movimentação e Física do Jogador
    jogador.movimento()
    jogador.pulo()
    jogador.gravidade()
    jogador.colisao()

    camera_x = jogador.x - 80
    if camera_x < 0:
        camera_x = 0

    if cooldown_tiro > 0:
        cooldown_tiro -= 1

    # 2. Movimentação e Física dos Inimigos
    for inimigo in inimigos:
        inimigo.movimento(jogador)
        inimigo.ataque(jogador)

    if jogador.hp <= 0:
        jogador.hp = 0
        estado_jogo = GAME_OVER
        sons.tocar_som(sons.SOM_GAME_OVER)
        return

    # 3. Colisões Inimigo-Inimigo
    for i in range(len(inimigos)):
        for j in range(i + 1, len(inimigos)):
            inimigos[i].colisao_inimigo(inimigos[j])

    # 4. Disparo de Projéteis Normais
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and cooldown_tiro == 0:
        novo_projetil = Projetil(jogador.x, jogador.y, jogador.direcao)
        projetis.append(novo_projetil)
        
        # NOVO: Usa a variável do jogador em vez do número 20 fixo
        cooldown_tiro = jogador.limite_cooldown_tiro 
        
        criar_efeito(efeitos, jogador.x, jogador.y + 10, 10, 3)
        sons.tocar_som(sons.SOM_TIRO)

    # 5. Colisão Projétil-Inimigo
    for projetil in projetis[:]:
        projetil.movimento()

        for inimigo in inimigos:
            inimigo_esquerda = inimigo.x - 10
            inimigo_direita = inimigo.x + 6
            inimigo_cima = inimigo.y - 10
            inimigo_baixo = inimigo.y + 6

            projetil_esquerda = projetil.x
            projetil_direita = projetil.x + 5
            projetil_cima = projetil.y
            projetil_baixo = projetil.y + 5

            if (
                projetil_direita > inimigo_esquerda
                and projetil_esquerda < inimigo_direita
                and projetil_baixo > inimigo_cima
                and projetil_cima < inimigo_baixo
            ):
                inimigo.hp -= projetil.dano
                if projetil in projetis:
                    projetis.remove(projetil)
                criar_efeito(efeitos, inimigo.x, inimigo.y, 7, 3)
                break

    # 5.5 Colisão Ataque Especial (Melee) - Inimigo
    for ataque in ataques_especiais[:]:
        ataque.movimento()
        
        # Apaga o ataque apenas quando o tempo da animação acabar naturalmente
        if ataque.tempo_vida <= 0:
            ataques_especiais.remove(ataque)
            continue

        for inimigo in inimigos:
            inimigo_esquerda = inimigo.x - 10
            inimigo_direita = inimigo.x + 6
            inimigo_cima = inimigo.y - 10
            inimigo_baixo = inimigo.y + 6

            ataque_esquerda = ataque.x
            ataque_direita = ataque.x + 16
            ataque_cima = ataque.y
            ataque_baixo = ataque.y + 16

            if (
                ataque_direita > inimigo_esquerda
                and ataque_esquerda < inimigo_direita
                and ataque_baixo > inimigo_cima
                and ataque_cima < inimigo_baixo
            ):
                # Se o ataque ainda não bateu em ninguém, causa o dano
                if ataque.dano > 0:
                    inimigo.hp -= ataque.dano
                    ataque.dano = 0  # Descarrega o ataque para não bater várias vezes seguidas
                    criar_efeito(efeitos, inimigo.x, inimigo.y, 9, 8)
                
                # O comando "remove(ataque)" foi apagado daqui!
                break

    # 6. Remoção de Inimigos Mortos
    for inimigo in inimigos[:]:
        if inimigo.hp <= 0:
            inimigos.remove(inimigo)
            inimigos_derrotados += 1
            contador_kills_upgrade += 1
            
            if contador_kills_upgrade >= 3:
                estado_jogo = UPGRADE
                contador_kills_upgrade = 0
                
            subiu_nivel = jogador.ganhar_xp(10)
            criar_efeito(efeitos, inimigo.x, inimigo.y, 8, 8)

            if subiu_nivel:
                criar_efeito(efeitos, jogador.x, jogador.y, 11, 15)
                sons.tocar_som(sons.SOM_LEVEL_UP)
            else:
                sons.tocar_som(sons.SOM_INIMIGO_DERROTADO)
        
    if len(inimigos) == 0:
        estado_jogo = VITORIA
        sons.tocar_som(sons.SOM_VITORIA)


def draw():

    if estado_jogo == MENU:
        desenhar_menu()
        return

    mapa.desenhar_fundo_paralaxe_2(camera_x)
    mapa.desenhar_fundo_paralaxe_1(camera_x)
    mapa.desenhar_mapa_principal(camera_x)

    if jogador.hp > 0:
        jogador.desenhar(camera_x)

    for inimigo in inimigos:
        inimigo.desenhar(camera_x)

    for projetil in projetis:
        projetil.desenhar(camera_x)

    for ataque in ataques_especiais:
        ataque.desenhar(camera_x)

    desenhar_efeitos(efeitos, camera_x)

    desenhar_hud(
        jogador,
        tempo_partida,
        inimigos_derrotados
    )

    if estado_jogo == GAME_OVER:
        desenhar_game_over()
    elif estado_jogo == VITORIA:
        desenhar_vitoria()
    
    elif estado_jogo == UPGRADE:
        pyxel.rect(20, 20, 120, 100, 0)
        pyxel.rectb(20, 20, 120, 100, 7)
        
        pyxel.text(35, 30, "ESCOLHA UM UPGRADE", 10)
        
        pyxel.rect(30, 50, 100, 20, 1)
        pyxel.text(45, 57, "1 - Ataque Melee", 7)
        
        pyxel.rect(30, 80, 100, 20, 2)
        pyxel.text(45, 87, "2 - Tiro Mais Rapido", 7) # NOVO TEXTO


pyxel.init(161, 161)
pyxel.load("my_resource.pyxres")
sons.configurar_sons()
pyxel.mouse(True)
pyxel.run(update, draw)