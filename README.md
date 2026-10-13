# Vampiro-CLT

Jogo de plataforma desenvolvido em Python utilizando a biblioteca Pyxel.

## Controles

* **A**: mover para a esquerda
* **D**: mover para a direita
* **Espaço**: pular
* **Botão esquerdo do mouse**: atirar

## Objetivo

Sobreviva por 120 segundos enquanto novas ondas de inimigos aparecem durante a partida.

## Mecânicas

* Movimento horizontal do jogador
* Pulo e gravidade
* Inimigos que perseguem o jogador
* Diferentes tipos de inimigos
* Velocidade, vida e dano diferentes por tipo de inimigo
* Spawn aleatório de inimigos
* Sistema de ondas a cada 20 segundos
* Limite de inimigos simultâneos
* Sistema de vida
* Sistema de dano
* Projéteis
* Hitbox dos projéteis
* Animação dos personagens
* Câmera com movimentação horizontal
* Tilemap para o cenário
* Sistema de XP e upgrades
* Vitória ao sobreviver 120 segundos

## Inimigos

Os inimigos perseguem o jogador horizontalmente.

Tipo 1 é o inimigo comum.

Tipo 2 é mais lento e resistente.

Tipo 3 é mais rápido e possui vida intermediária.

Novos inimigos aparecem fora da tela conforme o tempo da partida aumenta.

## Tecnologias

* Python
* Pyxel
* Git
* GitHub

## Como executar

Instale o Pyxel:

```bash
pip install pyxel
```

Depois execute:

```bash
python main.py
```

## Estrutura

```text
Vampiro-CLT/
│
├── main.py
├── jogador.py
├── inimigo.py
├── projetil.py
├── efeitos.py
├── mapa.py
├── sons.py
├── telas.py
├── musica.py
├── my_resource.pyxres
└── README.md
```

## Projeto

Projeto desenvolvido para aprendizado de programação e desenvolvimento de jogos utilizando Python e Pyxel.
