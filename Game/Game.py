import pygame
from pygame.locals import *


altura = 800
largura = 394
janela_aberta = True
x = 400 
y = 300

persona = [pygame.image.load("img\persona_parado.png"),pygame.image.load("img\persona_mov1.png"),
pygame.image.load("img\persona_mov2.png"),pygame.image.load("img\persona_mov3.png"),pygame.image.load("img\persona_mov4.png")]

Cenario = "img\cenario1.png"


#Inicializa a tela
pygame.init()


#Titulo da tela
pygame.display.set_caption("ThinkTitleLater")


#Define o tamanho da tela
tela = pygame.display.set_mode((altura,largura))


#Carrega o fundo
fundo = pygame.image.load(Cenario)


#Cria um looping para manter a janela aberta
while janela_aberta:
    #Adiciona o fundo
    tela.blit(fundo,(0,0))
    tela.blit(persona[0],(x,y))
    #Atualiza o frame
    pygame.display.update()

    for event in pygame.event.get():
        #Se for iniciado um evento de quit ele fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False            
    tecla = pygame.key.get_pressed()
    if tecla[K_LEFT]:
        x -= 1
        tela.blit(persona[1],(x,y))
        pygame.display.update()
        tela.blit(persona[2],(x,y))
        pygame.display.update()
        tela.blit(persona[3],(x,y))
        pygame.display.update()
    if tecla[K_RIGHT]:
        x += 1
        tela.blit(persona[1],(x,y))
        pygame.display.update()
        tela.blit(persona[2],(x,y))
        pygame.display.update()
        tela.blit(persona[3],(x,y))
        pygame.display.update()
    if tecla[K_UP]:
        y -= 1
        tela.blit(persona[1],(x,y))
        pygame.display.update()
        tela.blit(persona[2],(x,y))
        pygame.display.update()
        tela.blit(persona[3],(x,y))
        pygame.display.update()
    if tecla[K_DOWN]:
        y += 1
        tela.blit(persona[1],(x,y))
        pygame.display.update()
        tela.blit(persona[2],(x,y))
        pygame.display.update()
        tela.blit(persona[3],(x,y))
        pygame.display.update()