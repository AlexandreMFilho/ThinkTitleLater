import pygame
from pygame.locals import *

#Variáveis com a ALTURA e LARGURA da tela
altura = 800
largura = 394
#Variável com o status atual da tela
janela_aberta = True
#Variáveis com as posições inicias do personagem
x = 400 
y = 300
#Vetor que carrega todas as imagens do personagem
persona = [pygame.image.load("img\persona_parado.png"),pygame.image.load("img\persona_mov1.png"),
pygame.image.load("img\persona_mov2.png"),pygame.image.load("img\persona_mov3.png"),pygame.image.load("img\persona_mov4.png")]
#Variável com o Diretório do cenário
Cenario = "img\cenario1.png"

#Inicializa a tela
pygame.init()

#Titulo da tela
pygame.display.set_caption("ThinkTitleLater")

#Define o tamanho da tela
tela = pygame.display.set_mode((altura,largura))

#Carrega o fundo
fundo = pygame.image.load(Cenario)

#Função que anima o personagem
def movimento():
    tela.blit(persona[1],(x,y))
    pygame.display.update()
    tela.blit(persona[2],(x,y))
    pygame.display.update()
    tela.blit(persona[3],(x,y))
    pygame.display.update()

#Cria um looping para manter a janela aberta
while janela_aberta:

    #Adiciona o fundo
    tela.blit(fundo,(0,0))
    #Adiciona o personagem
    tela.blit(persona[0],(x,y))
    #Atualiza o frame
    pygame.display.update()

    for event in pygame.event.get():
        #Se for iniciado um evento de quit ele fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False      

    #Recebe a tecla digitada              
    tecla = pygame.key.get_pressed()

    #Se seta para ESQUERDA
    if tecla[K_LEFT]:
        x -= 1
        movimento()
    #Se seta para DIREITA
    if tecla[K_RIGHT]:
        x += 1
        movimento()
    #Se seta para CIMA
    if tecla[K_UP]:
        y -= 1
        movimento()
    #Se seta para BAIXO
    if tecla[K_DOWN]:
        y += 1
        movimento()