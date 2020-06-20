import pygame
from pygame.locals import *

altura = 800
largura = 394
janela_aberta = True
x = 400 
y = 300
velocidade = 1
corBranca = (255,255,255)
Dir_Persona_Parado = "img\persona_parado.png"
Cenario = "img\cenario1.png"

#Inicializa a tela
pygame.display.init()

#Titulo da tela
pygame.display.set_caption("ThinkTitleLater")

#Define o tamanho da tela
tela = pygame.display.set_mode((altura,largura))

#Carrega imagem
persona = pygame.image.load(Dir_Persona_Parado)
fundo = pygame.image.load(Cenario)

#Cria um looping para manter a janela aberta
while janela_aberta:
    for event in pygame.event.get():
        #Se for iniciado um evento de quit ele fecha a janela
        if event.type == pygame.QUIT:
            janela_aberta = False
    #Recebe a tecla digitada
    comandos = pygame.key.get_pressed()
    #Se for seta para cima
    if comandos[pygame.K_UP]:
        y -= velocidade
    #Se for seta para baixo
    if comandos[pygame.K_DOWN]:
        y += velocidade
    #Se for seta para esquerda
    if comandos[pygame.K_LEFT]:
        x -= velocidade 
    #Se for seta para direita
    if comandos[pygame.K_RIGHT]:
        x += velocidade    

    tela.blit(fundo,(0,0))
    #Torna a imagem visível
    tela.blit(persona,(x,y))
    #Atualiza o frame
    pygame.display.update()            