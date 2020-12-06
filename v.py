## pip instalal pygame
from b import limparTela
from b import *

import random
import string
import time
import pygame
nome = input("\n Insira seu nome: ")
email = input("\n Insira seu e-mail: ")
registro(nome, email)
limparTela()
pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Coletando as letrasç")
largura = 1080
altura = 600
alturaLetra = 150
larguraLetra = 100
letras = string.ascii_uppercase
letra = random.choice(letras)
preto = (0,0,0)
display = pygame.display.set_mode((largura, altura))


# devemos passar uma tupla como parametro - largura e altura
tela = pygame.display.set_mode( (largura,altura) )
relogio = pygame.time.Clock()

# loading image
fundo = pygame.image.load("OIP.jpg")
cesta = pygame.image.load("cesta.png")
cestaLargura = 177
cestaAltura = 200
cestaPosicaoX =650
cestaPosicaoY = 397
cestaMovimentoX = 0
cestaMovimentoY = 0
velocidadeCesta = 14
letraPosicaoX = random.randrange(0, largura - 100)
letraPosicaoY = 0
letraVelocidade = 5
def escrevendoPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("letras coletadas: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead():
    font = pygame.font.SysFont(None, 60)
    texto = font.render("\n Poxa você deixou passar a letra!", True, (0, 0, 0))
    display.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(3)
contador = 0
def aparecerL():
      font = pygame.font.SysFont(None, 150)
      texto = font.render(letra, True, (0, 0, 0))
      display.blit(texto, (letraPosicaoX, letraPosicaoY))
      pygame.display.update()   
contador = 0
for turma in range(40, 100):
    codigo = ''.join(random.choice(letras) for _ in range(4))
while True:
    # função fill define a cor de fundo da tela
      tela.blit(fundo, (0, 0))
      escrevendoPlacar(contador)
    
    #  devolve uma lista de eventos da tela []
      for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                  pygame.quit()
                  quit()
            if evento.type == pygame.KEYDOWN:
                  if evento.key == pygame.K_LEFT:
                        cestaMovimentoX = velocidadeCesta * -1
                  elif evento.key == pygame.K_RIGHT:
                        cestaMovimentoX = velocidadeCesta
            if evento.type == pygame.KEYUP:
                  cestaMovimentoX = 0
                  cestaMovimentoY = 0
      cestaPosicaoX = cestaPosicaoX + cestaMovimentoX
      cestaPosicaoY = cestaPosicaoY + cestaMovimentoY
      if cestaPosicaoX < 0:
            cestaPosicaoX = 0
      elif cestaPosicaoX > largura - cestaLargura:
            cestaPosicaoX = largura - cestaLargura
      display.blit(cesta, (cestaPosicaoX, cestaPosicaoY))
      if letraPosicaoY > altura:
            letraPosicaoY = 10 - alturaLetra
            letraVelocidade = letraVelocidade + 1
            if letraVelocidade >= 10:
                  letraVelocidade = 8
                  letraPosicaoX = random.randrange(0, largura - 100)
            letra = random.choice(letras)
      letraPosicaoY = letraPosicaoY + letraVelocidade
      aparecerL()
      if letraPosicaoY > altura:
            dead()
            letraVelocidade = 1
            letraPosicaoY = 0 - alturaLetra
            contador = 0
      # Verificando Colisões
      if cestaPosicaoY < letraPosicaoY + alturaLetra:
            if cestaPosicaoX < letraPosicaoX and cestaPosicaoX + cestaLargura > letraPosicaoX or letraPosicaoX+larguraLetra > cestaPosicaoX and letraPosicaoX+larguraLetra < cestaPosicaoX+cestaLargura:
                  letraPosicaoY = 10 - alturaLetra
                  letraVelocidade = letraVelocidade + 1
                  letraPosicaoX = random.randrange(50,750)
                  contador += 1
                  letra = random.choice(letras)
      letraPosicaoY = letraPosicaoY + letraVelocidade
      aparecerL()
      pygame.display.update()
      relogio.tick(60)