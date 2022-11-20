import random
import sys

import pygame

from Level.level import level
from Level.settings import *
from Personagem.Bala import Bala
from Personagem.Personagem import Personagem
from Personagem.Zumbi import Zumbi

clock = pygame.time.Clock()
largura = 1200
altura = 700 

pygame.init()
tela = pygame.display.set_mode((largura, altura))
level = level(piece_main,tela)


#imagemFundo = pygame.image.load('Sprites/bg.jpg')
pygame.display.set_caption("Pupo's attack")
all_sprites = pygame.sprite.Group()

tiros = pygame.sprite.Group()
jogando = True
enemies = pygame.sprite.Group()

# for i in range(5):
#     zumbi = Zumbi(random.randrange(0, largura), 350)
#     enemies.add(zumbi)
scroll = 0 
ground_image = pygame.image.load('Sprites/ground.png').convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []


while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('i')
                #jogador.shoot(all_sprites,tiros)


    hits = pygame.sprite.groupcollide(enemies, tiros, True, True)
    for hit in hits:
        m = Zumbi(random.randrange(0, largura), 350)
        all_sprites.add(m)
        enemies.add(m)
    tela.fill('black')
    level.run()
    #enemies.draw(tela)
    
    pygame.display.update()
    #all_sprites.draw(tela)
    
    clock.tick(60)
