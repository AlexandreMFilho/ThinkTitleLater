import pygame
from pygame.locals import *
altura = 800
largura = 600
janela_aberta = True

#Inicializa a tela
pygame.display.init()

#Titulo da tela
pygame.display.set_caption("ThinkTitleLater")
#Define o tamanho da tela
tela = pygame.display.set_mode((altura,largura))
#Carrega a imagem
fundo = pygame.image.load("img\Battleground3.png")

#Cria um looping para manter a janela aberta
while janela_aberta:
    for event in pygame.event.get():
        #Se for iniciado um evento de quit ele fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False
    #Torna a imagem visível
    tela.blit(fundo, (0,0))
    #Atualiza o frame
    pygame.display.update()            

