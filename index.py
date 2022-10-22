import pygame
import sys
import random
from Personagem.Personagem import Personagem
from Personagem.Zumbi import Zumbi
from Personagem.Bala import Bala

clock = pygame.time.Clock()
largura = 890
altura = 750

pygame.init()
imagemFundo = pygame.image.load('Sprites/bg.jpg')
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("RPG do SI")
all_sprites = pygame.sprite.Group()
jogador = Personagem()
all_sprites.add(jogador)
tiros = pygame.sprite.Group()
jogando = True
grupo_de_alvos = pygame.sprite.Group()

for i in range(5):
    zumbi = Zumbi(random.randrange(0, largura), random.randrange(0, altura))
    grupo_de_alvos.add(zumbi)

while jogando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                jogador.shoot(all_sprites,tiros)

    all_sprites.update()

    tela.blit(imagemFundo, (0, 0))
    grupo_de_alvos.draw(tela)
    jogador.colocar(tela)
    pygame.display.update()
    all_sprites.draw(tela)
    pygame.display.flip()
    clock.tick(60)
